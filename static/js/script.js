/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
//domain name validation

$('#domainname').on('keyup', function(){
    if(!validateDomain($(this).val())){
        alert("invalid domain");
        // $('.rez').text('invalid domain')

    }else{
        $('.rez').text('valid domain')

    }
});

function validateDomain(the_domain)
  {
    // strip off "http://" and/or "www."
    the_domain = the_domain.replace("http://","");

    the_domain = the_domain.replace("www.","");

    var reg = /^(?!:\/\/)([a-zA-Z0-9-]+\.){0,5}[a-zA-Z0-9-][a-zA-Z0-9-]+\.[a-zA-Z]{2,64}?$/gi;
    return reg.test(the_domain);
  } // end validateDomain()

//username validation

 function CheckAll() {

    var length = document.getElementById('username').value.length;
    var value = document.getElementById('username').value;

    for (var i = 0; i < length; i++) {
        if (!(/^[0-9a-zA-Z_.-]+$/.test(value))) {
            alert("username must be made of characters and numbers only");
            return false;
        }else{

            return true;
        }

    }

  }
