//	Michael Trinh
//	MikuRio
//	https://github.com/Mikur/MikuRio
// 	7/10/15
// 	The beginning of it all!

"use strict";

(function()
{
	var player;

	function $(id) { return document.getElementById(id); }

	window.onload = function()
	{
		// 2. This code loads the IFrame Player API code asynchronously.
		//var tag = document.createElement('script');
		//tag.src = "https://www.youtube.com/iframe_api";
		//var firstScriptTag = document.getElementsByTagName('head')[0];
		//firstScriptTag.appendChild(tag);

		document.querySelector("button").onmouseover = changeColors;
		document.querySelector("button").onmouseleave = changeBackColors;
		//$("skip").onclick = skipVideo;
		//$("playintro").onclick = watchVideo;
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
/*
	function skipVideo()
	{
		$("intro").style.display = "none";
		//$("vid").pause();
		//$("vid").currentTime = 0;
		player.stopVideo();
		$("mainpage").style.display = "initial";
		$("song").play();
		document.body.style.backgroundImage = "url('IMG_0815.jpg')";
	}

	function watchVideo()
	{
		$("intro").style.display = "initial";
		$("mainpage").style.display = "none";
		player.playVideo();
		//$("vid").play();
		$("song").pause();
		$("song").currentTime = 0;
	}

	// 3. This function creates an <iframe> (and YouTube player)
	//    after the API code downloads.
	window.onYouTubeIframeAPIReady = function() 
	{
		player = new YT.Player('player', 
		{
			events: 
			{
				'onReady': onPlayerReady,
			}
		});
	}

	// 4. The API will call this function when the video player is ready.
	function onPlayerReady(event)
	{
		event.target.playVideo();
	}
	
	function stopVideo() 
	{
		player.stopVideo();
	}
*/
}
)();