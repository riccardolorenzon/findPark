var findparkApp = angular.module('findPark', ['uiGmapgoogle-maps']);

findparkApp.config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        //    key: 'your api key',
        v: '3.17',
        libraries: 'weather,geometry,visualization'
    });
});

findparkApp.controller('mapCtrl', function ( $scope, $http, $log, $interval, $timeout, uiGmapGoogleMapApi) {
    uiGmapGoogleMapApi.then(function (maps) {
    $scope.map = {
        center: {latitude: 45.4627338, longitude: 9.1777322 },
        zoom: 12,
        bounds: {northeast: {latitude: 45.4627338, longitude: 9.1777322}, southwest: {latitude: 45.4627338, longitude: 9.1777322}},
        events: {
            bounds_changed :
                function(e){
                    //alert(e.bounds.northeast.latitude);
                    //alert($scope.map.bounds);
                    //TODO: trigger new drivers creations based on new bounds
                }
        }
    };

    // given bounds and center i need to find random points between the fist and the third quarter of the cartesian plane
    // lat [+90, -90] longitude [+180, -180]
    // Average point between 2 points, formula based on Talete theorem
    var firtsQuarterPointX = $scope.map.bounds.northeast.longitude + $scope.map.center.longitude / 2;
    var firtsQuarterPointY = $scope.map.bounds.northeast.latitude + $scope.map.center.latitude / 2;
    var thirdQuarterPointX = $scope.map.bounds.southwest.longitude + $scope.map.center.longitude / 2;
    var thirdQuarterPointY = $scope.map.bounds.southwest.latitude + $scope.map.center.latitude / 2;

    $scope.paths = [];
    var obj = {};
    $scope.drivers = [];
    $scope.drivers_details = [];
    var num_drivers = 3;
    var driver_obj = {};

    for (i = 0; i < num_drivers; i++)
    {
        var obj = {
            id: 0,
            coords: {
                latitude: 45.4627338,
                longitude: 9.1777322
            },
            icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/yellow.png",
            options: {
                draggable: false,
                labelAnchor: "100 0",
                labelClass: "marker-labels"
            }
        }
        $scope.drivers.push(obj);
    }

    var alice = {
        id: 0,
        coords: {
            latitude: 45.4627338,
            longitude: 9.1777322
        },
        icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/yellow.png",
        options: {
            draggable: false,
            labelAnchor: "100 0",
            labelClass: "marker-labels"
        }
    };
    var bob = {
        id: 0,
        coords: {
            latitude: 45.4627338,
            longitude: 9.1777322
        },
        options: {
            draggable: false,
            labelAnchor: "100 0",
            labelClass: "marker-labels"
        },
        icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/red.png",
        events: {}
    };

    var chuck = {
        id: 0,
        coords: {
            latitude: 45.4627338,
            longitude: 9.1777322
        },
        options: {
            draggable: false,
            labelAnchor: "100 0",
            labelClass: "marker-labels"
        },
        icon: "http://maps.google.com/intl/en_us/mapfiles/ms/micons/green.png",
        events: {}
    };

    $scope.drivers.push(alice);
    $scope.drivers.push(bob);
    $scope.drivers.push(chuck);

    var details = {};
    details.json = {};
    details.step = 0;
    details.latestChange = new Date();

    var point = {'latitude': -90 + 180 * Math.random(), 'longitude': -180 + 360 * Math.random()};
    details.start = "Porta+Ticinese,+Piazza+24+Maggio,+20136+Milano";
    details.end = "Porta+Garibaldi,+Piazza+XXV+Aprile,+Milano,+MI";

    $scope.drivers_details.push(details);
    $scope.drivers_details.push(details);
    $scope.drivers_details.push(details);

    for (i = 0; i < num_drivers; i++) {
        driver = $scope.drivers[i];
        $scope.$watch('$scope.drivers[i].coords', function (newValue, oldValue, scope) {
            currentTime = new Date();
            if (currentTime - $scope.drivers_details[i].latestChange > stopTimeout) {
                // i-th driver parked
                console.log("driver number " + i + ": parked");
                $http.post('/api/parkingspots/', {status: 'open', 'latitude': driver.coords.latitude,
                    'longitude': driver.coords.longitude, 'area': null })
                    .success(function (data, status) {
                    })
                    .error(function (data, status, headers, config) {
                        $scope.restData = "error on sending data to the server: " + status;
                    });
                $scope.driver_details[i].latestChange = currentTime;
            }
        }, true);
    }

    function fnsuccess(data, status, id, step, marker, index) {
        var jsonObj = data;
        obj.id = id;
        obj.stroke = {
            color: '#60' + id + '0FB',
            weight: 2
        };
        obj.visible = true;
        if (typeof jsonObj.routes == "undefined") {
            step = 0;
            return;
        }
        var step = jsonObj.routes[0].legs[0].steps[step];

        end_location = {};
        end_location.latitude = step.end_location.lat;
        end_location.longitude = step.end_location.lng;

        marker.coords.latitude = end_location.latitude;
        marker.coords.longitude = end_location.longitude;

        if (step % 4 == 0) {
            // wait a longer period to the next iteration
            $timeout(function () {
                $scope.simulation(index);
            }, Math.floor((Math.random() * WaitingTimeMax) + 1) * 10);
        }
        else {
            $timeout(function () {
                $scope.simulation(index);
            }, Math.floor((Math.random() * WaitingTimeMax) + 1));
        }
    };

    checkStep = function (jsonObj, step) {
        if (typeof  jsonObj.routes == "undefined")
            return 0;

        if (typeof  jsonObj.routes[0].legs == "undefined")
            return 0;

        if (step == jsonObj.routes[0].legs[0].steps.length - 1) {
            return 0;
        }
        return step;
    };

    var WaitingTimeMax = 10000;

    $scope.simulation = function (index) {
        driver = $scope.drivers[index];
        driver_details = $scope.drivers_details[index];
        $scope.drivers_details[index].step = checkStep(driver_details.json, driver_details.step);
        if (driver_details.step == 0 || driver_details.json.routes == []) {
            $http.get('/proxy/gmapsdirections/' + driver_details.start + '/' + driver_details.end + '/')
                .success(function (data, status) {
                    driver_details.json = JSON.parse(JSON.stringify(data));
                    fnsuccess(driver_details.json, status, 1, driver_details.step, driver, index);
                })
                .error(function (data, status, headers, config) {
                    $scope.restData = "errore nel ricevimento dati json ";
                });
        }
        else {
            fnsuccess(driver_details.json, status, 1, driver_details.step, driver, index);
        }
        $scope.drivers_details[index].step += 1;

    };

    stopTimeout = 1000;
    driver = $scope.drivers[0];

    driver_details = $scope.drivers_details[0];
    $timeout(function () {
        $scope.simulation(0);
    }, 1000);

    driver = $scope.drivers[1];

    driver_details = $scope.drivers_details[1];
    $timeout(function () {
        $scope.simulation(1);
    }, 1000);

    driver = $scope.drivers[2];

    driver_details = $scope.drivers_details[2];
    $timeout(function () {
        $scope.simulation(2);
    }, 1000);
    for (i = 0; i < num_drivers; i++) {
    }
    });



  });