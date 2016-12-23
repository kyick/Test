/**
 * Show the select critical points attributes
 */

/* Show Google Map of the select Route */
function showGraph(cellid) {
	alert(cellid);
}

/* Show Google Map of the select Route */
function showMap(route) {
	/* Removed old one first */
	var myNode = document.getElementById("route");
	while (myNode.firstChild) {
		myNode.removeChild(myNode.firstChild);
	}
	
	var img = document.createElement('img')
		
	if (route == 'BL_TO_UMDNJ') {
		img.setAttribute("src", "/static/pnaa/images/pnaaumdnj.png");
	}
	else {
		img.setAttribute("src", "/static/pnaa/images/pnaajfk.png");
	}
	img.setAttribute("alt", "route");
	document.getElementById("route").appendChild(img);
    
}

