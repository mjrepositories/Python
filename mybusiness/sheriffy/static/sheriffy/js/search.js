function myFunction() {
    srh_thing = document.querySelector('#id_thing');
    beginning = srh_thing.value[0].toUpperCase();
    ending = srh_thing.value.substring(1);
    srh_thing.value = beginning + ending;

    srh_city = document.querySelector('#id_city_name');
    beginning_city = srh_city.value[0].toUpperCase();
    ending_city = srh_city.value.substring(1);
    srh_city.value = beginning_city + ending_city;
}

function myClearFunction() {
    srh_thing_once = document.querySelector('#id_naming');
    srh_thing_once.value = "";

    srh_zone = document.querySelector('#id_zone');
    srh_zone.value = "";

    srh_category = document.querySelector('#id_category');
    srh_category.value = "";

    srh_city_once = document.querySelector('#id_city_name');
    srh_city_once.value = "";
}