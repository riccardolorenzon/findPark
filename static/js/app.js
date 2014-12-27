angular.module('findPark', ['uiGmapgoogle-maps'])
.controller('mapCtrl', function ($scope) {
  $scope.map = { center: { latitude: 45.6702345, longitude: 12.2350815 }, zoom: 10 };
});