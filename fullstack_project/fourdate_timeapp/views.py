from django.shortcuts import render
from datetime import datetime, timedelta
def datetime_offset(request):
    current_datetime = datetime.now()
    datetime_four_hours_ago = current_datetime - timedelta(hours=4)
    datetime_four_hours_ahead = current_datetime + timedelta(hours=4)
    datetime_four_days_ago = current_datetime - timedelta(days=4)
    datetime_four_days_ahead = current_datetime + timedelta(days=4)
    context = {
        'current_datetime': current_datetime,
        'datetime_four_hours_ago': datetime_four_hours_ago,
        'datetime_four_hours_ahead': datetime_four_hours_ahead,
        'datetime_four_days_ago': datetime_four_days_ago,
        'datetime_four_days_ahead': datetime_four_days_ahead,
    }
    
    return render(request, 'fourdate_timeapp/datetime_offset.html', context)