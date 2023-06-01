from nc.news.models import Category


def copy_to_postgresql():
    print("copy_to_postgresql")

    categorie_names = [
        "Thời sự",
        "Thế giới",
        "Kinh doanh",
        "Giải trí",
        "Thể thao",
        "Pháp luật",
        "Giáo dục",
        "Sức khỏe",
        "Đời sống",
        "Du lịch",
        "Khoa học",
        "Khác",
    ]

    for categorie_name in categorie_names:
        Category.objects.update_or_create(name=categorie_name)
