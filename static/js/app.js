var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.controller('mapCtrl', function ($scope, $http, $timeout) {
  $scope.map = {center: {latitude: 45.4627338, longitude: 9.1777322 }, zoom: 8, bounds: {}};
  // get directions from <origin> to <destination>
  // TODO this call is necessary for each point in the simulation
  $scope.paths = [];
  var obj ={};


  $http.get('/proxy/gmapsdirections/milan/turin')
      .success(function(data, status) {
            var jsonObj = JSON.parse(JSON.stringify(data));
            obj.id = 1;
            obj.stroke =  {
                color: '#6060FB',
                weight: 2
            };
            obj.visible = true;
            $scope.polylines = [];
            for (var rIndex = 0; rIndex < jsonObj.routes.length; rIndex++) {
                var route = jsonObj.routes[rIndex];
                for(var lIndex = 0; lIndex < route.legs.length; lIndex ++){
                    var leg = route.legs[lIndex];
                    for(var sIndex = 0; sIndex < leg.steps.length; sIndex++){
                        var step = leg.steps[sIndex];
                        if (typeof obj.path == "undefined")
                        {
                            obj.path = [];
                        }
                        start_location = {};
                        start_location.latitude = step.start_location.lat;
                        start_location.longitude = step.start_location.lng;

                        end_location = {};
                        end_location.latitude = step.end_location.lat;
                        end_location.longitude = step.end_location.lng;
                        /*
                        obj.path.push(start_location);
                        obj.path.push(end_location);
                        */
                        $scope.polylines[0] = obj;
                        $scope.polylines[0].path.push(start_location);
                        $scope.polylines[0].path.push(end_location);
                        /*$timeout(
                            function(obj, start_location, end_location){
                                $scope.polylines[0].path.push(start_location);
                                $scope.polylines[0].path.push(end_location);},
                            0);
                        */
                    }
                }
            }
      })
      .error(function(data, status, headers, config) {
            $scope.restData = "errore nel ricevimento dati json ";
      });
  });