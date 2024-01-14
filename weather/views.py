from django.shortcuts import render

# Create your views here.

# Views buat login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from weather.forms import UserAdminCreationForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import LoginForm

from .models import WeatherData

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('test')
            else:
                form.add_error(None, "Invalid email or password.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect ke halaman login setelah registrasi berhasil
    return render(request, 'register.html', {'form': form})

def test_view(request):
    return render(request, 'test.html')


# Views buat forecast
def load_weather_data_from_csv():
    try:
        # Ganti 'data_cuaca_januari.csv' sesuai dengan nama file yang Anda gunakan
        file_path = 'weather/cuaca.csv'

        # Ubah cara membaca file CSV
        with open(file_path, 'r') as file:
            csv_content = file.read()
        df = pd.read_csv(StringIO(csv_content), parse_dates=['Tanggal'], dayfirst=True)

        # Membuat objek WeatherData untuk setiap baris dalam file CSV
        weather_data_list = []
        for index, row in df.iterrows():
            weather_data = WeatherData(
                tanggal=row['Tanggal'],
                tavg=row['Tavg'],
                rh_avg=row['RH_avg'],
                ff_avg=row['ff_avg']
            )
            weather_data_list.append(weather_data)

        # Menggunakan bulk_create untuk memasukkan sekaligus ke dalam database
        WeatherData.objects.bulk_create(weather_data_list)

        return True
    except Exception as e:
        print(f"Error loading weather data from CSV: {e}")
        return False

def tavg_forecast(request):
    # Load actual weather data from the database
    actual_data = WeatherData.objects.all()
    actual_index = [data.tanggal.strftime('%Y-%m-%d') for data in actual_data]
    actual_values = [data.tavg for data in actual_data]

    # Load forecasted data (replace this with your forecasting logic)
    forecast_index = ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06", "2024-01-07"]
    forecast_values = [25.5, 26.0, 24.5, 23.0, 22.5, 24.0, 26.5]

    # Prepare days of the week for the card display
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    context = {
        'actual_index': actual_index,
        'actual_values': actual_values,
        'forecast_index': forecast_index,
        'forecast_values': forecast_values,
        'days_of_week': days_of_week,
    }

    return render(request, 'forecast/tavg_forecast.html', context)

def rhavg_forecast(request):
    # Load actual weather data from the database
    actual_data = WeatherData.objects.all()
    actual_index = [data.tanggal.strftime('%Y-%m-%d') for data in actual_data]
    actual_values = [data.rhavg for data in actual_data]

    # Load forecasted data (replace this with your forecasting logic)
    forecast_index = ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06", "2024-01-07"]
    forecast_values = [60.0, 62.0, 58.0, 55.0, 57.5, 61.0, 63.5]

    # Prepare days of the week for the card display
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    context = {
        'actual_index': actual_index,
        'actual_values': actual_values,
        'forecast_index': forecast_index,
        'forecast_values': forecast_values,
        'days_of_week': days_of_week,
    }

    return render(request, 'forecast/rhavg_forecast.html', context)

def ffavg_forecast(request):
    # Load actual weather data from the database
    actual_data = WeatherData.objects.all()
    actual_index = [data.tanggal.strftime('%Y-%m-%d') for data in actual_data]
    actual_values = [data.ffavg for data in actual_data]

    # Load forecasted data (replace this with your forecasting logic)
    forecast_index = ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05", "2024-01-06", "2024-01-07"]
    forecast_values = [12.0, 14.0, 11.5, 10.0, 9.5, 13.0, 15.0]

    # Prepare days of the week for the card display
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    context = {
        'actual_index': actual_index,
        'actual_values': actual_values,
        'forecast_index': forecast_index,
        'forecast_values': forecast_values,
        'days_of_week': days_of_week,
    }

    return render(request, 'forecast/ffavg_forecast.html', context)