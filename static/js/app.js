var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.controller('mapCtrl', function ($scope, $http) {
  $scope.map = { center: { latitude: 45.6702345, longitude: 12.2350815 }, zoom: 10 };
  // get directions from <origin> to <destination>
  // TODO this call is necessary for each point in the simulation

  $http.get('/proxy/gmapsdirections/srirangam/trichy')
      .success(function(data, status) {
            var jsonObj = JSON.parse(JSON.stringify(data));
            for (var rIndex = 0; rIndex < jsonObj.routes.length; rIndex++) {
                var route = jsonObj.routes[rIndex];
                for(var lIndex = 0; lIndex < route.legs.length; lIndex ++){
                    var leg = route.legs[lIndex];
                    for(var sIndex = 0; sIndex < leg.steps.length; sIndex++){
                        var step = leg.steps[sIndex];
                        start_location = step.polyline.start_location;
                        end_location = step.polyline.end_location;
                    }
                }
            }
      })
      .error(function(data, status, headers, config) {
            $scope.restData = "errore nel ricevimento dati json ";
      });
  });