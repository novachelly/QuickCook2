import React, {Fragment} from 'react';

const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector("nav");

menuBtn.addEventListener("click", function () {
  menuBtn.classList.toggle("active");
  nav.classList.toggle("active");
})

window.addEventListener("scroll", function () {
  if (window.pageYOffset > 4) {
    nav.classList.add("scrolled");
  } else {
    nav.classList.remove("scrolled");
  }
})

$(document).ready(function(){

  $('.input').focus(function(){
    $(this).parent().find(".label-txt").addClass('label-active');
  });

  $(".input").focusout(function(){
    if ($(this).val() == '') {
      $(this).parent().find(".label-txt").removeClass('label-active');
    };
  });

});

var firstName = "";
		var lastName = "";
		var email = "";
		var dType = "";
		var receipt = "";
		var anon = "";
		var list = "";
		var amount = "";
		
		$('.set-amount').autoGrow(0);
		
		/*
			if(isiPad || jQuery.browser.mobile){
				$('#team').hide()
				$('.team-mobile').show();	
			}else{
				$('#team').show()
				$('.team-mobile').hide();
			}
		*/
		
		//Set & Highlight Donation Amount
		$(".button").click(function(){
			$(".button").removeClass("selected");
			$(this).addClass("selected");
			
			$(this).find("input").focus();
		});
		
		//Grow the donation box if they type more than 4 numbers
		$(".set-amount").keyup(function(){
			
			if (this.value != this.value.replace(/[^0-9\.]/g, '')) {
		       this.value = this.value.replace(/[^0-9\.]/g, '');
		    }

		});
		
		
		$("input").on("change", function(){
			// $(".donation-box").css("height", "500px");
			
			firstName = $("#firstName").val();
			lastName = $("#lastName").val();
			email = $("#email").val();
			
			if ( $("#one-time").prop( "checked" ) ){
				dType = "One-Time";
			}
			if ( $("#monthly").prop( "checked" ) ){
				dType = "Monthly";
			}

		});
// <Fragment>
// function jresults() {
//     <h2>Your Recipe Match!</h2>
//         if (number = 1) {
//             <div>
//             <img src={{recipe_info,image}}/>
//             <h3>{{recipe_info, title}}</h3>
//             <a href={{recipe_info,sourceUrl}}>See the Recipe</a>
//             </div>;
//         else if (number = 2) {    
//             <div>
//             <img src={{recipe_info, image}}/>
//             <h3>{{recipe_info, title}}</h3>
//             <a href={{recipe_info, sourceUrl}}>See the Recipe</a>
//             </div>
//             <div>
//             <img src={{recipe_info1, image}}/>
//             <h3>{{recipe_info1, title}}</h3>
//             <a href={{recipe_info1, sourceUrl}}>See the Recipe</a>
//             </div>;
//         else {
//             <div>
//             <img src={{recipe_info, image}}/>
//             <h3>{{recipe_info, title}}</h3>
//             <a href={{recipe_info, sourceUrl}}>See the Recipe</a>
//             </div>
//             <div>
//             <img src={{recipe_info1, image}}/>
//             <h3>{{recipe_info1, title}}</h3>
//             </div>
//             <div>
//             <a href={{recipe_info1, sourceUrl}}>See the Recipe</a>
//             <img src={{recipe_info2, image}}/>
//             <h3>{{recipe_info2, title}}</h3>
//             <a href={{recipe_info2, sourceUrl}}>See the Recipe</a>
//             </div>;
// }
// </Fragment>
