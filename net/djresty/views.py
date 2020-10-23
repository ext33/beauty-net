from djresty.rest import RestyView, resty, RestyResponse


class TestRestyView(RestyView):
    @resty(url='test1')
    def test_api(self, request):
        return RestyResponse({'kek': 1337}, safe=False)

    @resty(url='test2')
    def test_api2(self, request):
        return RestyResponse({'kek': 1488}, safe=False)


class TestRestyView2(TestRestyView):
    @resty(url='test3')
    def test_api3(self, request):
        return RestyResponse({'kek': 1234}, safe=False)

    @resty(url='test3/<str:id>/')
    def test_api4(self, request, id):
        return RestyResponse({'kek': id}, safe=False)
