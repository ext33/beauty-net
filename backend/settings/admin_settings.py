admin_ui_tweaks = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "accent": "accent-navy",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "sidebar": "sidebar-dark-lightblue",
}

admin_settings = {
    'site_title': 'beauty-net',
    'site_logo': None,  # 'logos/logo.svg',
    'site_header': 'beauty-net',
    'welcome_sign': 'Авторизация',
    'copyright': 'beauty-net',

    # Field name on user model that contains avatar image
    'user_avatar': 'logos/user.svg',

    #############
    # User Menu #
    #############
    'usermenu_links': [
        {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############
    'show_sidebar': True,
    'navigation_expanded': True,
    'hide_apps': [],
    'hide_models': [],
    'order_with_respect_to': ['accounts', 'polls'],

    'icons': {
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },

    #############
    # UI Tweaks #
    #############
    "custom_css": 'css/admin.css',
    "custom_js": None,

    "show_ui_builder": False,

    "changeform_format": "single",

    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}