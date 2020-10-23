from functools import wraps

from django import forms
from django.http import JsonResponse, HttpResponse
from django.urls import path

from .plugins import RestyPlugin, ExceptionRestyResponse, RestyExtraParams


class RestyResponse(JsonResponse):
    pass


def resty(url: str = '', name: str = '', methods: list = None, form: forms.Form = None,
          plugins: 'list[RestyPlugin]' = [], csrf_exempt=False) -> callable:
    def wrapper(f: callable) -> callable:
        f.__setattr__('url', url if url else f.__name__)
        f.__setattr__('name', name if name else f.__name__)
        f.__setattr__('methods', methods)
        f.__setattr__('form', form)
        f.__setattr__('csrf_exempt', csrf_exempt)

        @wraps(f)
        def wrapped(self, request, *args, **kwargs) -> HttpResponse:
            # If class method, we passed None, because path doesnt send us self param
            # how to fix:
            # We must create second wrapper in get_urls for wrap memorize self arg
            # This is not required now, but maybe it help in future
            for plug in plugins:
                try:
                    ret = plug.exec(request, *args, **kwargs)
                    if isinstance(ret, RestyExtraParams):
                        kwargs.update(ret)
                except ExceptionRestyResponse as e:
                    return e.r
            return f(self, request, *args, **kwargs)

        return wrapped

    return wrapper


class RestyViewMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__
        parents = [b for b in bases if isinstance(b, RestyViewMeta)]
        if not parents:
            return super_new(cls, name, bases, attrs, **kwargs)
        new_class = super_new(cls, name, bases, attrs, **kwargs)
        _meta = getattr(bases[0], '_meta', {'api': []})
        _meta['api'] += [x for x in attrs.values() if (callable(x) and getattr(x, 'url', None))]
        setattr(bases[0], '_meta', _meta)
        return new_class


class RestyView(metaclass=RestyViewMeta):
    namespace = None
    name = None

    def __init__(self, name='', namespace=None):
        self.name = name
        self.namespace = namespace

    def get_urls(self):
        def wrap(wrap_self, f):
            def wrapper(*args, **kwargs):
                return f(wrap_self, *args, **kwargs)

            wrapper.csrf_exempt = f.csrf_exempt
            return wrapper

        urlpatterns = [
            path(x.url, wrap(self, x), name=x.name) for x in self._meta['api']
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), self.namespace, self.name
