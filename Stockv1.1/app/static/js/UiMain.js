$(function () {
	//----------------------上传头像---------------------------/
	$('#fxxking-arrow').click(function () {
  $('#fxxking-window').css('transform', 'scale(.11,.22)').css('left','-269px').css('top','-104px').css('z-index','-1').css('border-radius','50%');
        $('#fxxking-float').css('width', 'fit-content');
 });

    $('#fxxking-float').hover(function () {
        $('.btm').css('opacity', '1').css('top', '-20px');
    });
    $('#fxxking-float').mouseleave(function () {
        $('.btm').css('opacity', '0').css('top', '0px');
    });

    $('.upload-profile-img').click(function () {
        $('#fxxking-window').css('transform', 'scale(1,1)').css('left','250px').css('top','0').css('z-index','100').css('border-radius','30px');
        $('#fxxking-float').css('width', '250px');
    });
    //多选按钮判断
    $(".checkS").click(function () {
        //取出选中按钮的id值默认为1
        var s = $(this).attr('id');
        console.log(s);
        //判断是否为1并修改输入框样式
        if (Number(s)) {
            //如果点击按钮值为1 则遍利其他的按钮值是否为0并修改其他按钮的状态
            for (var i = 0; i < $('.checkS').length; i++) {
                //当其他元素值为0时并且id值不为当前选中值的id 那么就修改其id值为1并修改按钮状态
                if (Number($('.checkS').eq(i).attr('id') == 0) && (($('.checkS').eq(i).attr('id')) != ($(this).attr('id')))) {

                    $('.checkS').eq(i).attr("id", '1').css('color', '').css('border', '1px solid rgb(222,222,222)');
                }
            }
            //修改点击按钮的状态和值改为0
            $(this).css('color', '#ffaf02').css('border', '1px solid #ffaf02').css('outline', 'none').attr("id", '0');
        } else {
            //如果按钮值为0时则 再次把值改为1 并修改其状态
            $(this).css('color', '').css('border', '1px solid rgb(222,222,222)').attr("id", '1');
        }

    });

    /*------------------------上传头像--------------------------*/
            var input = document.querySelector('#file-input');
            var preview = document.querySelector('#u-chosen-img');

            input.style.opacity = 0;

            input.addEventListener('change', updateImageDisplay);

            function updateImageDisplay() {
              while(preview.firstChild) {
                preview.removeChild(preview.firstChild);
              }

          var curFiles = input.files;
          if(curFiles.length === 0) {
            // var para = document.createElement('p');
            para.textContent = 'No files currently selected for upload';
            preview.appendChild(para);
          } else {
            var list = document.createElement('ol');
            preview.appendChild(list);
            for(var i = 0; i < curFiles.length; i++) {
              var listItem = document.createElement('li');
              // var para = document.createElement('p');
              if(validFileType(curFiles[i])) {
                // para.textContent = 'File name ' + curFiles[i].name + ', file size ' + returnFileSize(curFiles[i].size) + '.';
                var image = document.createElement('img');
                image.src = window.URL.createObjectURL(curFiles[i]);

                listItem.appendChild(image);
                // listItem.appendChild(para);

              } else {
                // para.textContent = 'File name ' + curFiles[i].name + ': Not a valid file type. Update your selection.';
                listItem.appendChild(para);
              }

              list.appendChild(listItem);
            }
          }
        }

        var fileTypes = [
              'image/jpeg',
              'image/pjpeg',
              'image/png',
            'image/jpg'
            ];

        function validFileType(file) {
          for(var i = 0; i < fileTypes.length; i++) {
            if(file.type === fileTypes[i]) {
              return true;
            }
          }

          return false;
        }
	  function returnFileSize(number) {
				  if(number < 1024) {
					return number + 'bytes';
				  } else if(number >= 1024 && number < 1048576) {
					return (number/1024).toFixed(1) + 'KB';
				  } else if(number >= 1048576) {
					return (number/1048576).toFixed(1) + 'MB';
				  }
				}


			var drop_img = document.getElementById("fxxking-arrow")
			drop_img.addEventListener('click', drop_fxxking_img)
			function drop_fxxking_img() {
				$('#u-chosen-img img').remove()
			}


    /*------------------------上传头像--------------------------*/


    //广告按钮点击事件
    $("#adButton").click(function(){
        $(".main").css("filter","blur(7px)").css("transform","scale(1.05)");
        $("#realAd").css("transform",'scale(1)');
        $("body").css('transition','1s');
        $("#adText").css('transition','0.1s');

    });
    $("#exitAd").click(function(){
        $(".main").css("filter","blur(0)").css("transform","scale(1)");
        $("#realAd").css("transform",'scale(0)');
        $("body").css('transition','1s');

    });
	//广告页面彩蛋
	var nspin = 90
	$("#spin").click(function(){
		if(nspin == 90){
			$("body").css("transform",'rotate(90deg) scale(0.5)');
			nspin = 0
		}else{
			$("body").css("transform",'rotate(0deg) scale(1)');
			nspin = 90
		}

	})
	var matrixes = ['matrix3d(0.5, 0.2, 0, 0.0005, -0.7, 0.87, 0.19, 0.00001, 0.9, 0, 0.51, 0, 0, 100, 0.5, 1.4)',
					'matrix3d(1, 0, 0, 0,0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)',
					'matrix3d(0.7, 0.1, 0.7, -0.0004, -0.127, 0.57, 0.19, 0.00001, 0.5, 0, 0.71, 0, -400, -150, 0.5, 1)',
					'matrix3d(1, 0, 0, 0,0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)',
					'matrix3d(0.8, 0.2, 0, -0.0004, 0.1, 0.87, 0.19, 0.00001, 0.9, 0, 0.51, 0, -300, -60, 0.5, 1.1)',
					'matrix3d(1, 0, 0, 0,0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)'
	]
	var x = 0
	$("#rotate").click(function(){
		if(x==6){
			x=0;
		}
		$("body").css("transform",matrixes[x]);
		x=x+1
	})
	// $("#return").click(function(){
	// 	$("body").css("transform",'rotate(0)');
	// 	$('body').css('filter', 'invert(0%)');
	// 	$('body').css('animation','none');
	// })
	var deg=0
	$("#mirror").click(function(){
		deg=deg+180
		$('body').css('transform', 'rotateY('+deg+'deg)');
	})
	var strng = true
	$("#strange").click(function(){
		if(strng){
			$('body').css('transform','rotate(4deg)');
			strng=false
		}else{
			$('body').css('transform','rotate(0deg)');
			strng=true
		}
	})
	var inverter = 0
	$("#invert").click(function(){
		if(inverter == 0){
			inverter = 100
		}else{
			inverter = 0
		}
		$('body').css('filter', 'invert('+inverter+'%)');
	})
	rainbow = true
	$("#rainbow").click(function(){
		if(rainbow){
			$('body').css('animation','a 10s infinite linear');
			rainbow = false
		}else{
			$('body').css('animation','none');
			rainbow = true
		}
	});
	///////////////////////////////////////////////////v1.2 这次修改内容/////////////////////////////////////////////////////////////
    $("#cxk").click(function() {
        $("#cxkjn").css("animation", 'cxk 3s').css('animation-delay', '3s');
        $('#centerCxk').css('animation', 'cxkcenter 10s');
        $('#cxklanqiu').css('animation', 'cxklanqiu 10s linear');
        $('.slowDanmu').css('animation', 'danmuSlide 8s  linear').css('animation-delay', '2s');
        $('.fastDanmu').css('animation', 'danmuSlide 5s  linear').css('animation-delay', '3s');
        $('.superfastDanmu').css('animation', 'danmuSlide 3s  linear').css('animation-delay', '1s');
        $('.fourSiders').css('animation', 'spinblocks 10s 1 linear');
    });
    ///////////////////////////////////////////////////v1.2 这次修改内容/////////////////////////////////////////////////////////////
//-----------------------股票查询----------------------------
    function checkname() {
        $.ajax({
            url: '/stock',
            type: 'post',
            data: {storkcode: $('#input1').val()},
            async: false,
            dataType: 'json',
            success: function (data) {
                //data 响应回来的数据
                var html='';
                if (data) {

                    html += '<tr>';
                    html += '<td>' + data.stock_name + '</td>';
                    html += '<td>' + data.stock_no + '</td>';
                    html += '<td>' + data.current_price + '</td>';
                    html += '<td>' + data.fluctuation + '</td>';
                    html += '<td>' + data.fluctuation_by_percent + '%' + '</td>';
                    html += '<td>' + data.volume + '</td>';
                    html += '<td>' + data.turnover + '</td>';
                    html += '</tr>'
                }
                $('#textname').html('');
                html1=html.concat(html1);
                $('#ccc').html(html1);
            },
            error:function () {
                $('#textname').html('未查找到该股票')
            }
        });
    }
	//
    var html1 = '';
    $('#btn1').click(function () {
        checkname()
    });


//----------------------选择标签栏top-------------------------//
	$('.imgcl').click(function(){
		//1显示 0隐藏
		if ($(this).prop('value'))
			{
			$(this).find('div:last-child').css('display','block');
			$(this).find('div:nth-child(3)').attr('class','urlcenter');
			for (var i=0;i<$('.imgcl').length ;i++ )
			{
				if ($('.imgcl').eq(i).prop('value')==0)
				{
					$('.imgcl').eq(i).find('div:last-child').css('display','none');
					$('.imgcl').eq(i).prop('value','1');
					$('.imgcl').eq(i).find('div:nth-child(3)').attr('class','');
					$('.imgcl').css('background','');
					$('.imgcl').css("width","100px");
				}
			}
			$(this).prop('value','0');
			$(this).css('background','rgba(0,0,0,0.15)');
			$(this).css("width","300px");
			}
		else
			{
			$(this).prop('value','1')
			$(this).find('div:last-child').css('display','none');
			$(this).find('div:nth-child(3)').attr('class','');
			$(this).css('background','');
			$(this).css("width","100px");
			}

		});
			
		//1显示 0隐藏
		if ($('#li1').prop('value'))
			{
			$('#li1').find('div:last-child').css('display','block');
			$('#li1').find('div:nth-child(3)').attr('class','urlcenter');
			$('#li1').prop('value','0');
			$('#li1').css('background','rgba(0,0,0,0.15)');
			$('#li1').css("width","300px");
			}
		else
			{
			$('#li1').prop('value','1')
			$('#li1').find('div:last-child').css('display','none');
			$('#li1').find('div:nth-child(3)').attr('class','');
			$('#li1').css('background','');
			$('#li1').css("width","100px");
			}

		
		$('#div3,#div2,#div1').click(function(e){
			e.stopPropagation();
			});
		// $('#div2').click(function(e){
		// 	e.stopPropagation();
		// 	});
        // $('#div1').click(function(e){
		// 	e.stopPropagation();
		// 	});

/*-----------------------续费---------------------*/
		var div4=true;
		$('#axufei').click(function(){
			if (div4)
			{
				$('#div4').prop('class','div4-true');
				$('#div4 div').css('display','block');
				$('#div4').css("opacity",'1');
				div4=false;
			}
			else
			{
				$('#div4').prop('class','div4-false');
				// $('#div4 div').css('display','none');
				$('#div4').css("opacity",'0');

				div4=true;
			}
			
		});
		/*判断月还是年*/
		$("#div4Bz label").click(function(){

			$(this).parent('span').siblings().children('label').attr("class","unselect");
			
			if ( $(this).prev('input').attr('id')==='month')
			{
				$('#vip1').text('月');
			}else{
				$('#vip1').text('年');
			}
			$(this).attr("class","select");
		});
		/*限制不为100倍的数字*/
		$('.inputNu').change(function(){
			var number=$(this).val()%100

			if (number!=0)
			{
				$(this).prop('value','0');
				alert('请输入100的倍数')
			};
		});
		//判断充值金额

		$('#div4Cz span').click(function(){
			$('#div4Cz span').attr('id','');
			$(this).attr('id','span');
		});

		//充值会员
		$('#subVip').click(function () {
			if ($('#uname').text()=='未登录'){
				alert('未登录账户请登录后充值')
			}else {
				console.log($('#uname').text());
				$.ajax({
                    url:"/recharge",
                    type:"post",
                    data:{
                      'uname':$('#uname').text(),
                       'time': $('#vip1').text(),
						'number':$('#vip').val()
                    },
                    async:true,
                    dataType:"json",
					success:function(data){
                    	if(data.status){
							$('#vip10').text(data.time+'到期');
							$('#vip9').text(data.exe)
                  			alert(data.text)
                    	}else {
                    		alert(data.text)
						}
                      }


			 })
			}

		});
		//充值金钱
		$('#subRmb').click(function () {
			if ($('#uname').text()=='未登录') {
				alert('未登录账户请登录后充值')
            }else {$.ajax({
                    url: "/update_data",
                    type: "post",
                    data: {
                        'uname': $('#uname').text(),
                        'umoney': $('#span').children('.number').text()
                    },
                    async: true,
                    dataType: "json",
                    success: function (data) {
                        if (data.status) {
                            $('#umoney1').text(data.umoney);
                            $('#umoney2').text(data.uamt);
                            alert(data.text)
                        } else {
                            alert(data.text)
                        }
                    }


                })
            }
		})

		function formatDate(value) {
				console.log(value)
                var date = new Date(Number(value[0]),Number(value[1]),Number(value[2]),Number(value[3]),Number(value[4]),00).format("yyyy-MM-dd HH:mm");
                if (date == "1970-01-01 08:00") {
                    console.log('--');
                    return "--";
                }else{
                	console.log('date');
                    return date;}
            }
		$('#submit1').click(function () {
            var value = $('input[name=strtime]').val();
            value =  value.replace(/-/g,':').replace(' ',':');
            value=value.split(':');
			console.log(value)
            var date = formatDate(value);
			console.log(date)
        }),

		function ss() {

			var time = '2018-08-19';

			time = time.replace(/-/g,':').replace('',':');

			time = time.split(':');

			var myTime = new Date(time[0],(time[1]-1),time[2]);

			alert(myTime);

		};

		$('#buttonOP').click(function () {
			$.ajax({
                    url: "/04-stocklook",
                    type: "get",
                    data: {
                        'unumber1': $('#OP1').val(),
                        'unumber2': $('#OP2').val()
                    },
                    async: true,
                    dataType: "json",
                    success: function (data) {
                    	console.log(data.status)
                        if (data.status==1) {
                        	var html = '';
                        	for	(var i =0;i<data.lists.length;i++){
                        		html += '<tr>';
								html += '<th>' + data.lists[i][1] + '</th>';
								html += '<th>' + data.lists[i][0] + '</th>';
								html += '<th>' + data.lists[i][2] + '元/股</th>';
								html += '<th><input type="number" class="ajaxInpt" oninput="if(value>99999)value=99999;if(value.length>2)value=value.slice(0,5);if(value<1)value=1"></th>'
								html += '<th>'+'</th>';
								html += '<td><a href="javascript:voild(0)" class="ajaxA">买入</a></td>';
								html += '</tr>';
							}
							$('#buttonOP1').text(data.stcok),
                            $('#OP3').html(html);
                        } else {
                            alert(data.text)
                        }

                    }


                })

		});
		//设置动态生成的input绑定函数事件
		$('#OP3').on('change', '.ajaxInpt', function (){
			var summ=$(this).parent('th').prev('th').text().split('元')[0]*$(this).val();
			$(this).parent('th').next('th').html(summ.toFixed(2)+'元');
			});
		//购买股票
		$('#OP3').on('click', '.ajaxA', function (){
			var money=$(this).parent('td').prev('th').text()
			var stockname=$(this).parent('td').parent('tr').children('th:first-child').text();
			var stocknumber=$(this).parent('td').parent('tr').children('th:nth-child(2)').text();
			var stockprice=$(this).parent('td').parent('tr').children('th:nth-child(3)').text();
			var shands=$(this).parent('td').parent('tr').children('th:nth-child(4)').children('input').val()
			var r=confirm('你确认购买 "'+stockname+'" 股票总计: '+money)
			if (r){
			$.ajax({
				url: "/05-stockbuy",
                    type: "post",
                    data: {
                        'money': money,//多少钱
                        'stockname': stockname,//股票名字
                        'stocknumber': stocknumber,//股票号码
                        'shands': shands,//持股数量
                        'stockprice': stockprice//买入时价格
                    },
                    async: false,
                    dataType: "json",
					success:function (data) {
						if (data.status){
							$('#umoney1').text(data.umoney);
                            $('#umoney2').text(data.uamt);
                            $('#umoney3').text(data.stockMoney);
						alert(data.text)
						}else{
							alert(data.text)
						}
                    }

			})}
		})
		//查询股票
		$('#stockLook').click(function () {
			$.ajax({
				url: "/06-stocklook",
                    type: "post",
                    async: false,
                    dataType: "json",
					success:function (data) {
						if (data.status){
						alert(data.text);
						console.log(data.list);
							var html2='';
							for(var i=0;i<data.list.length;i++){
							html2+='<tr>';
								for(var r=0;r<data.list[i].length;r++){
									html2+='<th>'+data.list[i][r]+'</th>'
							}
							html2+='</tr>'
							}
							console.log(html2);
							$('#sss').html(html2)
						}else{
							alert(data.text)
						}
                    }

			})
        })


})

    


