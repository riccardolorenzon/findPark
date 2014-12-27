var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.controller('mapCtrl', function ($scope, $http) {
  $scope.map = { center: { latitude: 45.6702345, longitude: 12.2350815 }, zoom: 10 };
  $http.get('/proxy/gmapsdirections/srirangam/trichy')
      .success(function(data, status) {
                  
        })
      .error(function(data, status, headers, config) {
            $scope.restData = "errore nel ricevimento dati json ";
      });
  });