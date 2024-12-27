import angular from 'angular';

angular.module('alertController', ['alertService']).

controller('AlertDisplayController', ['Alert','$timeout', function(Alert) {
  var vm = this;

  vm.alert = Alert;
  vm.remove = index => {
    Alert.alerts.splice(index, 1);
  };
  vm.clearAll = function() {
    Alert.alerts = [];
  };

  
}]);
