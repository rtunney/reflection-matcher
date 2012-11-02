//func that looks up your name
// attach the action to the button

var keywords_by_name = {};
for (i=0; i < master_list.length; i++){
  keywords_by_name[master_list[i].name] = master_list[i].keywords
};

var people_by_keywords = {};
for (i=0; i < master_list.length; i++){
  for (el in master_list[i].keywords){
    var name = master_list[i].name;
    if (people_by_keywords[el] == undefined){
      people_by_keywords[el] = [name];
    }else{
      people_by_keywords[el].push(name);
    }
  }
};
console.log(people_by_keywords);

function get_keywords(name){
  return keywords_by_name[name]
};

function get_people(keyword){
  return people_by_keywords[keyword]
};

function display_keywords(){
  var my_name = document.getElementById('name');
  var keywords = get_keywords(my_name.value)
  kwlist = document.getElementById('kwlist');
  for (el in keywords){
    console.log(el);
    var listelement = document.createElement('li')
    listelement.innerHTML = el;
    kwlist.appendChild(listelement);
  }
};



button = document.getElementById('button');
button.addEventListener('click', display_keywords);