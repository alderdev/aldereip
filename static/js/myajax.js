

function showCustName(id)
{/* 帶出客戶編號的ajax */
	var xmlhttp;
	if (id=="")
	  {
		  document.getElementById("sap_no_customer").innerHTML="請輸入客戶編號";
		  //document.getElementById(id).innerHTML="œÐ¿é€JÄæŠìžê®Æ";
		  return;
	  }
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari

			xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	 		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }

	xmlhttp.onreadystatechange=function()
	{

    if (xmlhttp.readyState==4 &&xmlhttp.status==404){
      window.alert("無效的客戶編號");
      document.getElementById("title_customer").value = "";
      document.getElementById("sap_no_customer").focus() ;
      document.getElementById("sap_no_customer").selected = true;
      return;
    }


		if (xmlhttp.readyState==4 && xmlhttp.status==200)
	   {
  				var start = xmlhttp.responseText.indexOf("<span>")+6;
  				var end = xmlhttp.responseText.indexOf("</span>",start);
  				var x = xmlhttp.responseText.substring(start, end);

  			 	var str = x.split(',');
          document.getElementById("id_customer").value = str[0];
  				document.getElementById("sap_no_customer").value = str[1];
  				document.getElementById("title_customer").value = str[2];

	    }
	};

	xmlhttp.open("GET","/dpsed/customertitle/"+id+"/",true);
	xmlhttp.send();
}


function showProudct(id)
{/* 帶出客戶編號的ajax */
	var xmlhttp;
	if (id=="")
	  {
		  document.getElementById("sap_no_customer").innerHTML="請輸入客戶編號";
		  //document.getElementById(id).innerHTML="œÐ¿é€JÄæŠìžê®Æ";
		  return;
	  }
	if (window.XMLHttpRequest)
	  {// code for IE7+, Firefox, Chrome, Opera, Safari

			xmlhttp=new XMLHttpRequest();
	  }
	else
	  {// code for IE6, IE5
	 		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }

	xmlhttp.onreadystatechange=function()
	{

    if (xmlhttp.readyState==4 &&xmlhttp.status==404){
      window.alert("無效的料號");
      document.getElementById("product_desc").value = "";
      document.getElementById("id_product").focus() ;
      document.getElementById("sap_no_customer").selected = true;
      return;
    }

		if (xmlhttp.readyState==4 && xmlhttp.status==200)
	   {
  				var start = xmlhttp.responseText.indexOf("<span>")+6;
  				var end = xmlhttp.responseText.indexOf("</span>",start);
  				var x = xmlhttp.responseText.substring(start, end);

  			 	var str = x.split(',');
          document.getElementById("id_product").value = str[0];
  				document.getElementById("sap_no_product").value = str[1];
					document.getElementById("product_desc_span").value = str[2];
  				document.getElementById("product_desc").value = str[2];

	    }
	};

	xmlhttp.open("GET","/dpsed/productdesc/"+id+"/",true);
	xmlhttp.send();
}
