from django_filters import FilterSet, DurationFilter, TimeFilter, DateFilter
from .models import Post

class PostFilter(FilterSet):
    start_date = DateFilter(field_name="release_datetime", lookup_expr='gte')
    end_date = DateFilter(field_name="release_datetime", lookup_expr='lte')
    start_time = TimeFilter(field_name="release_datetime", lookup_expr='gte')
    end_time = TimeFilter(field_name="release_datetime", lookup_expr='lte')
    duration = DurationFilter(field_name="release_datetime")

    class Meta:
        model = Post
        fields = [
            'post_title', 'categories', 'start_date', 'end_date', 'start_time', 'end_time', 'duration', "post_type",
        ]

