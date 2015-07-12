//	Michael Trinh
//	MikuRio
//	https://github.com/Mikur/MikuRio
// 	7/10/15
// 	The beginning of it all!

"use strict";

(function()
{
	window.onload = function()
	{
		document.querySelector("button").onmouseover = changeColors;
		document.querySelector("button").onmouseleave = changeBackColors;
	};

	function changeColors()
	{
		var logo = document.querySelector("h1");
		logo.style.transition = "color 2s ease";
		logo.style.color = "#99CCFF";
	}

	function changeBackColors()
	{
		var logo = document.querySelector("h1");
		logo.style.transition = "color 2s ease";
		logo.style.color = "#CCFFFF";
	}
}
)();