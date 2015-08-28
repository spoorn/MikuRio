//	Michael Trinh
//	MikuRio
//	https://github.com/Mikur/MikuRio
// 	7/10/15
// 	The beginning of it all!

"use strict";

(function()
{
	function $(id) { return document.getElementById(id); }

	window.onload = function()
	{
		document.querySelector("button").onmouseover = changeColors;
		document.querySelector("button").onmouseleave = changeBackColors;
		$("skip").onclick = skipVideo;
		$("playintro").onclick = watchVideo;
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

	function skipVideo()
	{
		$("intro").style.display = "none";
		$("vid").pause();
		$("vid").currentTime = 0;
		$("mainpage").style.display = "initial";
		$("song").play();
		document.body.style.backgroundImage = "url('kaori2.jpg')";
	}

	function watchVideo()
	{
		$("intro").style.display = "block";
		$("mainpage").style.display = "none";
		$("song").currentTime = 0;
		$("vid").play();
		$("song").pause();
	}
}
)();