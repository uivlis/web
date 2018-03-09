 $('document').ready(function () {

   $('#comment').bind('input propertychange', function () {
     this.value = this.value.replace(/ +(?= )/g, '');

     if (this.value.length > 500) {
       this.value = this.value.substring(0, 500);
     }

     if (this.value.length) {
       $("#charcount").html(501 - this.value.length);
     }

   });

   $('#githubProfile').on('focus', function () {
     $('#githubProfileHelpBlock').hide();
     $('#githubProfile').removeClass('is-invalid');
   });

   $('#emailAddress').on('focus', function () {
     $('#emailAddressHelpBlock').hide();
     $('#emailAddress').removeClass('is-invalid');
   });

   $('#emailAddress').on('change', function () {
     var exp = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

     if (!exp.test(this.value)) {
       $('#emailAddress').addClass('is-invalid');
       $('#emailAddressHelpBlock').html('We could not validate that input as an email address').show();
     }
   });

   $('#submitFaucet').on('click', function (e) {
     e.preventDefault()

     if (e.target.hasAttribute('disabled') ||
       $('#githubProfile').is(['is-invalid']) ||
       $('#emailAddress').is(['is-invalid']) ||
       $('#githubProfile').val() === '' ||
       $('#emailAddress').val() === '') {
       _alert("Please make sure to fill out all fields.")
       return;
     }

     var faucetRequestData = {
       'githubProfile': $('#githubProfile').val().replace('@', ''),
       'ethAddress': $('#ethAddress').val(),
       'emailAddress': $('#emailAddress').val(),
       'comment': $('#comment').val(),
       'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
     }

     $.post('/api/v0.1/faucet/save', faucetRequestData)
       .done(function (d) {
         $('#primary_form').hide();
         $('#success_container').show();
       })

       .fail(function (response) {
        var message = response.responseJSON.message;
         $('#primary_form').hide();
         $('#fail_message').html(message);
         $('#fail_container').show();
       });
   })
 });