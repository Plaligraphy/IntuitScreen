from pyowm.owm import OWM
owm = OWM('233a80f0949773a2a747fda592388231')
mgr = owm.weather_manager()
one_call = mgr.one_call(lat=45.357132, lon=-122.84750)
print(one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None))

# Test Script (Not for Final Production use)
