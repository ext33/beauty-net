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
    'site_title': 'BEAUTY NET',
    'site_logo': None,  # 'logos/logo.svg',
    'site_header': 'BEAUTY NET',
    'welcome_sign': 'Авторизация',
    'copyright': 'BEAUTY NET',


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
    "custom_css": 'admin.css',
    "custom_js": None,

    "show_ui_builder": False,

    "changeform_format": "single",

    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}