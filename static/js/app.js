var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.controller('mapCtrl', function ($scope, $http) {
  $scope.map = { center: { latitude: 45.6702345, longitude: 12.2350815 }, zoom: 10 };
  $scope.restData = "stocazzo";
  $http.get('http://maps.googleapis.com/maps/api/directions/json?origin=srirangam&destination=trichy&sensor=false', {withCredentials: true})
      .success(function(data) {
        $scope.restData = data;
      })
      .error(function(data, status, headers, config) {
        $scope.restData = "errore nel ricevimento dati json ";
      });
  });