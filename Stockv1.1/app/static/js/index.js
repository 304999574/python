//验证码生成函数
function sum1(){
    var lists='23456789abcdefghgkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ';
    var number1=[];
    var charIndex=4;

    while (true)
    {
        var slice=parseInt(Math.random()*lists.length)

        if (0<=slice && slice <57)
        {
            if (number1.length==charIndex)
            {
                break
            }
            number1.push(lists[slice])
        }
    }
    var number2=number1.join('');

    $("#tishi").html("验证码:"+number2);
    console.log(number2)
    return number2
}
//验证码判断
function sum2(number2) {
    var number3=$('input[name=code]').val();
    if (number3.toUpperCase()== number2.toUpperCase())
    {
        return 1
    }else{
        return 0
    }
}



$(function(){
	
	$('#img1').css('height','300px');

	var number2=sum1();

    $('input[name=code]').blur(function () {
        var a=$('input[name=code]').val()
        if (a){
            var s=sum2(number2);
            if (s){
                alert("验证成功")
            }else{
                alert("验证码错误")
            }
    }
    });
    //记住密码状态栏
    var left=false;
    $('input[name=left]').click(function () {
        if (left){
            $(this).prop('checked','checked');
            left=false
        }else{
            $(this).prop('checked','');
            left=true
        }

    });
    //点击时
    $('#tishi').click(function () {
        number2=sum1()
    })

	$("#lastInput").click(function (){
	    if (sum2(number2)){
		$.ajax({
			url: '/login',
			type: 'post',
			data: {
			  uname:$("#uname").val(),
			  upwd:$("input[name=upwd]").val(),
              left:$('input[name=left]').prop('checked')
			},
			async: false,
			dataType: 'json',
			success: function (data) {
				alert(data.text);
				if ( data.status == 1)
				{
					 $(".input1").val('');
					window.location.href='/login'
				}else {
					$(".input1").val('');
				}
                }
            })
	    }else{
	        alert('验证码不相同请重新输入')
        }
    })


})