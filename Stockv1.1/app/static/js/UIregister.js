
	
// $('#img1').css('height','300px');
//查询用户名是否存在
function checkuname(){
	  var re = false;
	  $.ajax({
		  url:'/checkuname',
		  type:'get',
		  data:"uname="+$("#uname").val(),
		  async:true,
		  dataType:'json',
		  success:function (data){
			  if (data.status=='1'){
				  re=true; //设置用户名已存在状态
                  $("#uname-tip").css('color','#e23f40');
			  }else {
			     $("#uname-tip").css('color','#3addff').css('font-size','15px');
			  }
			  $("#uname-tip").html(data.text);
		  }
	  });
	  return re
  };

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
//判断验证码是否一样
function sum2(number2) {
    var number3=$('#code').val();
    if (number3.toUpperCase()==number2.toUpperCase())
    {
        return 1
    }else{
        return 0
    }
}
//判断密码是否一样
function checkupwd(){
    re = false;
    if($("input[name=upwd]").val() != $("input[name=upwd1]").val()){
        re = true;
        $('#pwd').html('密码不一致请重新输入').css('color','#e23f40')
    }else{
        $('#pwd').html('密码全部正确').css('color','#3addff')
    }
    return re

}

$(function(){
    $('#img1').css('height','300px');
    var number2=sum1();
    $('#code').blur(function () {
        var a=$('input[id=code]').val();
        if (a){
            var s=sum2(number2);
            if (s){
                alert("验证成功")
            }else{
                alert("验证码错误")
            }
        }
    });
    $('input[name=upwd1]').blur(function () {
        checkupwd()
    });

    $("#uname").blur(function(){
        checkuname()
    });
    $('#tishi').click(function () {
        number2=sum1()
    })



    $("#lastInput").click(function (){
        if (checkuname()||checkupwd()){
            alert("用户名已存在或密码不一致");
        }else{
            $.ajax({
                url: '/server',
                type: 'post',
                data: {
                  uname: $("#uname").val(),
                  upwd: $("input[name=upwd]").val()
                },
                async: true,
                dataType: 'json',
                success: function (data) {
                    alert(data.text);
                    if ( data.status == 1)
                    {
                         $(".input1").val('');
                        window.location.href='/loginregister'
                    }else{
                        $(".input1").val('');
                    }
                }
            })


        }
    })



})
