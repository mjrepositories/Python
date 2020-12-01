//Taking care of button 0

const realFileBtn_0 = document.getElementById('id_image_set-0-image');
const customBtn_0 = document.getElementById('custom_button_0');
const customText_0 = document.getElementById('custom_text_0');

customBtn_0.addEventListener('click',function(){
    realFileBtn_0.click();
})

realFileBtn_0.addEventListener('change',function(){
    if (realFileBtn_0.value){
        customText_0.innerHTML = realFileBtn_0.value.split('\\')[realFileBtn_0.value.split('\\').length-1];
        customText_0.style.display = 'inline'
    }
    else {
        customText_0.innerHTML =  'No file chosen'
    }
})

//take care of button 1
const realFileBtn_1 = document.getElementById('id_image_set-1-image');
const customBtn_1 = document.getElementById('custom_button_1');
const customText_1 = document.getElementById('custom_text_1');

customBtn_1.addEventListener('click',function(){
    realFileBtn_1.click();
})

realFileBtn_1.addEventListener('change',function(){
    if (realFileBtn_1.value){
        customText_1.innerHTML = realFileBtn_1.value.split('\\')[realFileBtn_1.value.split('\\').length-1];
        customText_1.style.display = 'inline'
    }
    else {
        customText_1.innerHTML =  'No file chosen'
    }
})

//take care of button 2
const realFileBtn_2 = document.getElementById('id_image_set-2-image');
const customBtn_2 = document.getElementById('custom_button_2');
const customText_2 = document.getElementById('custom_text_2');

customBtn_2.addEventListener('click',function(){
    realFileBtn_2.click();
})

realFileBtn_2.addEventListener('change',function(){
    if (realFileBtn_2.value){
        customText_2.innerHTML = realFileBtn_2.value.split('\\')[realFileBtn_2.value.split('\\').length-1];
        customText_2.style.display = 'inline'
    }
    else {
        customText_2.innerHTML =  'No file chosen'
    }
})

//take care of button 3
const realFileBtn_3 = document.getElementById('id_image_set-3-image');
const customBtn_3 = document.getElementById('custom_button_3');
const customText_3 = document.getElementById('custom_text_3');

customBtn_3.addEventListener('click',function(){
    realFileBtn_3.click();
})

realFileBtn_3.addEventListener('change',function(){
    if (realFileBtn_3.value){
        customText_3.innerHTML = realFileBtn_3.value.split('\\')[realFileBtn_3.value.split('\\').length-1];
        customText_3.style.display = 'inline'
    }
    else {
        customText_3.innerHTML =  'No file chosen'
    }
})

//take care of button 4
const realFileBtn_4 = document.getElementById('id_image_set-4-image');
const customBtn_4 = document.getElementById('custom_button_4');
const customText_4 = document.getElementById('custom_text_4');

customBtn_4.addEventListener('click',function(){
    realFileBtn_4.click();
})

realFileBtn_4.addEventListener('change',function(){
    if (realFileBtn_4.value){
        customText_4.innerHTML = realFileBtn_4.value.split('\\')[realFileBtn_4.value.split('\\').length-1];
        customText_4.style.display = 'inline'
    }
    else {
        customText_4.innerHTML =  'No file chosen'
    }
})

//take care of button 5
const realFileBtn_5 = document.getElementById('id_image_set-5-image');
const customBtn_5 = document.getElementById('custom_button_5');
const customText_5 = document.getElementById('custom_text_5');

customBtn_5.addEventListener('click',function(){
    realFileBtn_5.click();
})

realFileBtn_5.addEventListener('change',function(){
    if (realFileBtn_5.value){
        customText_5.innerHTML = realFileBtn_5.value.split('\\')[realFileBtn_5.value.split('\\').length-1];
        customText_5.style.display = 'inline'
    }
    else {
        customText_5.innerHTML =  'No file chosen'
    }
})

//take care of button 6
const realFileBtn_6 = document.getElementById('id_image_set-6-image');
const customBtn_6 = document.getElementById('custom_button_6');
const customText_6 = document.getElementById('custom_text_6');

customBtn_6.addEventListener('click',function(){
    realFileBtn_6.click();
})

realFileBtn_6.addEventListener('change',function(){
    if (realFileBtn_6.value){
        customText_6.innerHTML = realFileBtn_6.value.split('\\')[realFileBtn_6.value.split('\\').length-1];
        customText_6.style.display = 'inline'
    }
    else {
        customText_6.innerHTML =  'No file chosen'
    }
})

//take care of button 7
const realFileBtn_7 = document.getElementById('id_image_set-7-image');
const customBtn_7 = document.getElementById('custom_button_7');
const customText_7 = document.getElementById('custom_text_7');

customBtn_7.addEventListener('click',function(){
    realFileBtn_7.click();
})

realFileBtn_7.addEventListener('change',function(){
    if (realFileBtn_7.value){
        customText_7.innerHTML = realFileBtn_7.value.split('\\')[realFileBtn_7.value.split('\\').length-1];
        customText_7.style.display = 'inline'
    }
    else {
        customText_7.innerHTML =  'No file chosen'
    }
})


