/// <reference path="DefinitelyTyped/angularjs/angular.d.ts" />


class MyService {
    constructor() {
    }
    add(a:number, b:number):number {
        return a + b;
    }
}

interface MyScope extends ng.IScope {
    message: string;
    myService: MyService;
    action: Function;
}

class MyController {
    private scope: MyScope;
    private myService: MyService;

    constructor($scope:MyScope, myService:MyService){
        this.scope = $scope;
        this.myService = myService;

        this.scope.message = 'Hello, World!' + this.myService.add(1, 3);
        this.scope.action = angular.bind(this, this.action);
    }

    action() {
        this.scope.message = 'Goodbye, Everyone!';
    }
}

var appModule:ng.IModule = angular.module('app', []);

appModule.factory('myService', () => {
    return new MyService();
});
appModule.controller('myController', [
        '$scope', 'myService', ($scope, myService) => {
            return new MyController($scope, myService);
        }]);

