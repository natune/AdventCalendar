'use strics';

$(function(){
  const vm = {
    loginId: ko.observable(''),
    password: ko.observable(''),
    onClickLogin: function(){
      
    }
  }

  ko.applyBindings(vm, document.getElementById('loginContent'))
});
