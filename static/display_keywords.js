//func that looks up your name
// attach the action to the button

// var keywords_by_name = {};
// for (i=0; i < master_list.length; i++){
//   keywords_by_name[master_list[i].name] = master_list[i].keywords
// };

// var people_by_keywords = {};
// for (i=0; i < master_list.length; i++){
//   for (el in master_list[i].keywords){
//     var name = master_list[i].name;
//     if (people_by_keywords[el] == undefined){
//       people_by_keywords[el] = [name];
//     }else{
//       people_by_keywords[el].push(name);
//     }
//   }
// };
// console.log(people_by_keywords);

// function get_keywords(name){
//   return keywords_by_name[name]
// };

// function get_people(keyword){
//   return people_by_keywords[keyword]
// };

var user_name = document.getElementById('name').value

function display_keywords(){
  var name_input = document.getElementById('name');
  var keywords = get_keywords(name_input.value)
  kw_list = document.getElementById('kw_list');
  for (keyword in keywords){
    var keyword_li = document.createElement('li');
    keyword_li.innerHTML = keyword;
    display_people(keyword_li, keyword);
    kw_list.appendChild(keyword_li);
  }
};

function display_people(keyword_li, keyword){
 var people_list = document.createElement('ul');
    keyword_li.appendChild(people_list);
    people = people_by_keywords[keyword];
    for (var i=0; i<people.length; i++) {
      var person_li = document.createElement('li');
      person_li.innerHTML = people[i];
      people_list.appendChild(person_li);
    }
}

// function on_response (data, textStatus){
  
// }

function display_matches() {
  $.post('http://localhost:5000/', {fname: user_name}, function(data, textStatus){
    console.log(textStatus);
  });
}

button = document.getElementById('button');
button.addEventListener('click', display_matches);
