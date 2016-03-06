var MyService = (function () {
    function MyService() {
    }
    MyService.prototype.add = function (a, b) {
        return a + b;
    };
    return MyService;
})();

var MyController = (function () {
    function MyController($scope, myService) {
        this.scope = $scope;
        this.myService = myService;

        this.scope.message = 'Hello, World!' + this.myService.add(1, 3);
        this.scope.action = angular.bind(this, this.action);
    }
    MyController.prototype.action = function () {
        this.scope.message = 'Goodbye, Everyone!';
    };
    return MyController;
})();

var appModule = angular.module('app', []);

appModule.service('myService', function () {
    return new MyService();
});
appModule.controller('myController', [
    '$scope', 'myService', function ($scope, myService) {
        return new MyController($scope, myService);
    }]);
//# sourceMappingURL=sample-app.js.map
