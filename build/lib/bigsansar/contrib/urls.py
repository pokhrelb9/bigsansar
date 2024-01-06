from bigsansar.contrib.views import about_page, contact_page, index_page


path_handlers = {
        "": index_page,
        "/dashboard": index_page,
        "/about": about_page,
        "/contact": contact_page,
    }