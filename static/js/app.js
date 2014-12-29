var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.controller('mapCtrl', function ($scope, $http, $log, $timeout) {
  $scope.map = {center: {latitude: 45.6702345, longitude: 12.2350815 }, zoom: 12, bounds: {}};
  // get directions from <origin> to <destination>
  // TODO this call is necessary for each point in the simulation
  $scope.paths = [];
  var obj ={};
  $scope.polylines = [];

  $scope.alice = {
      id: 0,
      coords: {
        latitude: 45.6702345,
        longitude: 12.2350815
      },
      options: { draggable: false },
      events: {
        dragend: function (marker, eventName, args) {
          $log.log('marker dragend');
          var lat = marker.getPosition().lat();
          var lon = marker.getPosition().lng();
          $log.log(lat);
          $log.log(lon);

          $scope.alice.options = {
            draggable: false,
            labelContent: "lat: " + $scope.alice.coords.latitude + ' ' + 'lon: ' + $scope.alice.coords.longitude,
            labelAnchor: "100 0",
            labelClass: "marker-labels"
          };
        }
      }
    };

    $scope.bob = {
      id: 0,
      coords: {
        latitude: 50.6702345,
        longitude: 12.2350815
      },
      options: { draggable: false },
      events: {
        dragend: function (marker, eventName, args) {
          $log.log('marker dragend');
          var lat = marker.getPosition().lat();
          var lon = marker.getPosition().lng();
          $log.log(lat);
          $log.log(lon);

          $scope.bob.options = {
            draggable: false,
            labelContent: "lat: " + $scope.bob.coords.latitude + ' ' + 'lon: ' + $scope.bob.coords.longitude,
            labelAnchor: "100 0",
            labelClass: "marker-labels"
          };
        }
      }
    };

  $scope.chuck = {
      id: 0,
      coords: {
        latitude: 55.6702345,
        longitude: 12.2350815
      },
      options: { draggable: false },
      events: {
        dragend: function (marker, eventName, args) {
          $log.log('marker dragend');
          var lat = marker.getPosition().lat();
          var lon = marker.getPosition().lng();
          $log.log(lat);
          $log.log(lon);

          $scope.chuck.options = {
            draggable: false,
            labelContent: "lat: " + $scope.chuck.coords.latitude + ' ' + 'lon: ' + $scope.chuck.coords.longitude,
            labelAnchor: "100 0",
            labelClass: "marker-labels"
          };
        }
      }
    };


  function fnsuccess(data, status, id){
      $scope.polylines[id-1] = {};
      $scope.polylines[id-1].id = 1;
      $scope.polylines[id-1].stroke =  {
        color: '#60' + id + '0FB',
        weight: 2
      };
      $scope.polylines[id-1].visible = true;
      $scope.polylines[id-1].path = [];
        var jsonObj = JSON.parse(JSON.stringify(data));
        obj.id = id;
        obj.stroke =  {
            color: '#60' + id + '0FB',
            weight: 2
        };
        obj.visible = true;
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
                    $scope.paths[id-1] = obj;
                    $scope.paths[id-1].path.push(start_location);
                    $scope.paths[id-1].path.push(end_location);

                    //$scope.polylines[id-1].path.push(start_location);
                    //$scope.polylines[id-1].path.push(end_location);

                    $scope.alice.coords.latitude = end_location.latitude;
                    $scope.alice.coords.longitude = end_location.longitude;
                }
                 var step = leg.steps[leg.steps.length -1];
                 end_location = {};
                 end_location.latitude = step.end_location.lat;
                 end_location.longitude = step.end_location.lng;

                 //$scope.alice.coords.latitude = end_location.latitude;
                 //$scope.alice.coords.longitude = end_location.longitude;
            }
        }

        /*for (var i = 0; i < $scope.paths.length; i++) {
                var p = $scope.paths[i];
                for (var j = 0; j < p.path.length; j++) {
                    xpath = p.path[j];
                    $scope.polylines[id-1].path.push(xpath);
                }
         }*/
  }

  function sleep(milliseconds) {
      var start = new Date().getTime();
      for (var i = 0; i < 1e7; i++) {
          console.log('working');
        if ((new Date().getTime() - start) > milliseconds){
          break;
        }
      }
    }

  $scope.jsonAlice = {};

  $scope.startSimulation = function() {
      var boh;
      var boh2;
      $http.get('/proxy/gmapsdirections/Silea+TV/Duomo,+Treviso,+TV/')
          .success(function (data, status) {
            $scope.jsonAlice = JSON.parse(JSON.stringify(data));
            fnsuccess(data, status, 1);
          })
          .error(function (data, status, headers, config) {
              $scope.restData = "errore nel ricevimento dati json ";
          });
      //TODO timeout function with increasing step number
  }
  /*
  $http.get('/proxy/gmapsdirections/Carbonera+TV/Palazzo+dei+Trecento,+Treviso,+TV/')
      .success(function(data, status) {
            fnsuccess(data,status, 2);
      })
      .error(function(data, status, headers, config) {
            $scope.restData = "errore nel ricevimento dati json ";
      });

  $http.get('/proxy/gmapsdirections/Dosson+TV/Piazza+dei+Signori,+Treviso,+TV/')
      .success(function(data, status) {
            fnsuccess(data,status, 3);
      })
      .error(function(data, status, headers, config) {
            $scope.restData = "errore nel ricevimento dati json ";
      });
  */
  });