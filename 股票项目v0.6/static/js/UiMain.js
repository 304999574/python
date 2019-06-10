$(function () {
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
    //广告按钮点击事件
    $("#adButton").click(function(){
        $(".main").css("filter","blur(10px)").css("transform","scale(1.15)");
        $("#realAd").css("transform",'scale(1)');
    });
    $("#exitAd").click(function(){
        $(".main").css("filter","blur(0)").css("transform","scale(1)");
        $("#realAd").css("transform",'scale(0)');
    });

//-----------------------股票查询----------------------------
    function checkname() {
        $.ajax({
            url: '/',
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
    $('#input1').blur(function () {
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

		
		$('#div3').click(function(e){
			e.stopPropagation();
			})
		$('#div2').click(function(e){
			e.stopPropagation();
			})
        $('#div1').click(function(e){
			e.stopPropagation();
			})
/*-----------------------续费---------------------*/
		var div4=true;
		$('#axufei').click(function(){
			if (div4)
			{
				$('#div4').prop('class','div4-true');
				$('#div4 div').css('display','block');
				div4=false;
			}
			else
			{
				$('#div4').prop('class','div4-false');
				$('#div4 div').css('display','none');
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
		})
		/*限制不为100倍的数字*/
		$('.inputNu').change(function(){
			var number=$(this).val()%100

			if (number!=0)
			{
				$(this).prop('value','0')
				alert('请输入100的倍数')
			};
		})
		$('#div4Cz span').click(function(){
			$('#div4Cz span').attr('id','')
			$(this).attr('id','span')
		})
    

});
