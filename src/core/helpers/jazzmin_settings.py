JAZZMIN_SETTINGS = {
    "site_title": "Paycash Admin",
    "site_header": "Paycash",
    "search_model": "transaction.transaction",
    "user_avatar": None,
    # Links to put along the top menu
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "transaction.source"},
        {"model": "transaction.integration"},
    ],
    "usermenu_links": [
        {"name": "Support", "url": "https://easily.kz", "new_window": True},
        {"model": "transaction.source"},
        {"model": "transaction.integration"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": ['common.globalconfiguration', 'common.profile', 'authtoken.tokenproxy'],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "common": "fas fa-users",
        "common.company": "fas fa-building",
        "common.profile": "fas fa-user-cicle-o",
        "transaction.transaction": "fas fa-book",
        "transaction.user": "fas fa-bookmark"
    },
    "default_icon_parents": "fas fa-clone",
    "default_icon_children": "fas fa-circle-o",
    "related_modal_active": False,
    "language_chooser": False,
}