$(document).ready(function(){

    var wallet = document.querySelector('#profile #profileBlock #profilesDownContent #wallet');
    var transactoin = document.querySelector('#profile #profileBlock #profilesDownContent #transactoin .dropdown');

    wallet.visibility = "visible";
    wallet.position = "static";

    var page = document.getElementById('ProfilePage').value

    var Profile_Page_Now = 'wallet';

    if (page != Profile_Page_Now){
        var id = page;

        var Element_new = document.querySelector('#profile #profileBlock #profilesDownContent #' + id)
        var Element_old = document.querySelector('#profile #profileBlock #profilesDownContent #' + Profile_Page_Now)

        Element_old.style.visibility = "hidden";
        Element_old.style.position = "absolute";

        Element_new.style.visibility = "visible";
        Element_new.style.position = "static";



        Profile_Page_Now = id;
    }
    else{
        transactoin.style.visibility = "hidden";
        transactoin.style.position = "absolute";
    }

    $('#profilesUpChoice a')
    .on('click', function() {
        if(id == Profile_Page_Now) return 0;

        var id = this.className;


        if(id != "transactoin"){
            transactoin.style.visibility = "hidden";
            transactoin.style.position = "absolute";
        }
        else{
            transactoin.style.visibility = "visible";
            transactoin.style.position = "static";
        }

        var Element_new = document.querySelector('#profile #profileBlock #profilesDownContent #' + id)
        var Element_old = document.querySelector('#profile #profileBlock #profilesDownContent #' + Profile_Page_Now)

        Element_old.style.visibility = "hidden";
        Element_old.style.position = "absolute";

        Element_new.style.visibility = "visible";
        Element_new.style.position = "static";

        Profile_Page_Now = id;
    });

});