// MathJax Configuration
//
// v2 to v3 upgrade notes:
// - The CommonHTML.linebreaks option is not yet implemented (but may be in a future release)
// - The TeX.noUndefined.attributes option is not yet implemented (but may be in a future release)

function open_menu_on_load(elem){
  document.getElementById(elem).classList.toggle("show");
}

function open_menu_on_click(elem) { 
  var elemId = elem.id;
  var dropdownId = elem.id.concat("-ddowncontent");
  document.getElementById(dropdownId).classList.toggle("show");
  
  var dropdowns = document.getElementsByClassName("ddowncontent");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      if (dropdowns[i].id != dropdownId && dropdowns[i].classList.contains('show')) {
        dropdowns[i].classList.remove('show');
      }
    }
}

function test_function_one(elem) {
  var elemId = elem.id;
  var drowndownclass = elem.id.concat("-ddowncontent") 
  var dropdowns = document.getElementsByClassName(drowndownclass);
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
}