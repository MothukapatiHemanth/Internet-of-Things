<table border=2>
<tr><th>Humidity</th><th>Latitude</th><th>Longitude</th><th>Temperature</th><th>weather</th></tr>
%for item in data:
  <tr>
  <td>{{item['humidity']}}</td><td>{{item['latitude']}}</td><td>{{item['longitude']}}</td><td>{{item['temp']}}</td><td>{{item['weather']}}</td>
  </tr>
%end
</table>
