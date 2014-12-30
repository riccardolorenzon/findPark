var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.controller('mapCtrl', function ($scope, $http, $log, $interval) {
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
      icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/yellow.png",
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
      icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/red.png",
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
      icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/green.png",
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


  function fnsuccess(data, status, id, step, marker){

        $scope.polylines[id-1] = {};
        $scope.polylines[id-1].id = 1;
        $scope.polylines[id-1].stroke =  {
        color: '#60' + id + '0FB',
        weight: 2
        };
        $scope.polylines[id-1].visible = true;
        $scope.polylines[id-1].path = [];
        var jsonObj = data; //JSON.parse(JSON.stringify(data));
        obj.id = id;
        obj.stroke =  {
            color: '#60' + id + '0FB',
            weight: 2
        };
        obj.visible = true;

        var step =  jsonObj.routes[0].legs[0].steps[step];

        end_location = {};
        end_location.latitude = step.end_location.lat;
        end_location.longitude = step.end_location.lng;

        marker.coords.latitude = end_location.latitude;
        marker.coords.longitude = end_location.longitude;
  }

  function sleep(milliseconds) {
      var start = new Date().getTime();
      for (var i = 0; i < 1e7; i++) {
        if ((new Date().getTime() - start) > milliseconds){
          break;
        }
      }
    }

  checkStep = function(jsonObj, step)
  {
    if (typeof  jsonObj.routes == "undefined")
        return 0;
    if (step == jsonObj.routes[0].legs[0].steps.length - 1)
        {
            return 0;
        }
    return step;
  };


  $scope.jsonAlice = {};
  $scope.stepAlice = 0;

  $scope.jsonBob = {};
  $scope.stepBob = 0;

  $scope.jsonChuck = {};
  $scope.stepChuck = 0;

  $scope.simulation = function() {
      $scope.stepAlice = checkStep($scope.jsonAlice, $scope.stepAlice);
      //alice
      if($scope.stepAlice == 0) {
          $http.get('/proxy/gmapsdirections/Silea+TV/Duomo,+Treviso,+TV/')
              .success(function (data, status) {
                  $scope.jsonAlice = JSON.parse(JSON.stringify(data));
                  fnsuccess($scope.jsonAlice, status, 1, $scope.stepAlice, $scope.alice);
              })
              .error(function (data, status, headers, config) {
                  $scope.restData = "errore nel ricevimento dati json ";
              });
      }
      else
      {
          fnsuccess($scope.jsonAlice, status, 1, $scope.stepAlice, $scope.alice);
      }
      $scope.stepAlice +=1;

      //bob

      $scope.stepBob = checkStep($scope.jsonBob, $scope.stepBob);
      if($scope.stepBob == 0) {
          $http.get('/proxy/gmapsdirections/Carbonera+TV/Palazzo+dei+Trecento,+Treviso,+TV/')
              .success(function (data, status) {
                  $scope.jsonBob = JSON.parse(JSON.stringify(data));
                  fnsuccess($scope.jsonBob, status, 1, $scope.stepBob, $scope.bob);
              })
              .error(function (data, status, headers, config) {
                  $scope.restData = "errore nel ricevimento dati json ";
              });
      }
      else
      {
          fnsuccess($scope.jsonBob, status, 1, $scope.stepBob, $scope.bob);
      }
      $scope.stepBob +=1;

      //chuck

      $scope.stepChuck = checkStep($scope.jsonChuck, $scope.stepChuck);
      if($scope.stepChuck == 0) {
          $http.get('/proxy/gmapsdirections/Dosson+TV/Piazza+dei+Signori,+Treviso,+TV/')
              .success(function (data, status) {
                  $scope.jsonChuck = JSON.parse(JSON.stringify(data));
                  fnsuccess($scope.jsonChuck, status, 1, $scope.stepChuck, $scope.chuck);
              })
              .error(function (data, status, headers, config) {
                  $scope.restData = "errore nel ricevimento dati json ";
              });
      }
      else
      {
          fnsuccess($scope.jsonChuck, status, 1, $scope.stepChuck, $scope.chuck);
      }
      $scope.stepChuck +=1;

  }

  $interval($scope.simulation, 1000);

  });