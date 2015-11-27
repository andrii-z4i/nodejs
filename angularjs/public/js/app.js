var app = angular.module('TestApp', []);

app.controller('MainController', ['$http', function($http){
    this.name = "MainController";

    _this = this;
    this.get_additional_data = function() {
        $http.get('/additional').then(function(data){
            _this.name = data.data.name;
        });
    }
}]);