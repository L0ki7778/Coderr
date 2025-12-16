import django_filters as filter

class OfferFilter(filter.FilterSet):
    creator_id = filter.NumberFilter(field_name='user', distinct=True)
    min_price = filter.NumberFilter(field_name='details__price', lookup_expr='gte', distinct=True)
    max_delivery_time = filter.NumberFilter(field_name='details__delivery_time_in_days',lookup_expr='lte',distinct=True)