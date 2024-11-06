import streamlit as st
import utils as utl
from pathlib import Path
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import base64
import streamlit.components.v1 as components


st.set_page_config(
    page_title="DERM INSIGHT APP",
    page_icon="🧊",
    layout="wide",
)
utl.local_css("/Users/mac/appAI/streamlit.css")


# Hàm chuyển hình ảnh sang bytes và mã hóa base64
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Hàm tạo HTML cho hình ảnh đã mã hóa base64
def img_to_html(img_path, width="100px", height="80px"):
    img_html = f"<img src='data:image/png;base64,{img_to_bytes(img_path)}' style='width:{width}; height:{height};'>"
    return img_html

# Sử dụng hàm img_to_html để mã hóa logo và hình ảnh bên phải
logo_html = img_to_html('logo.png', width="100px", height="100px")  # Thay đường dẫn này bằng logo của bạn
right_image_html = img_to_html('anhbiamun.png', width="250px", height="230px")  # Thay đường dẫn bằng ảnh khác
bia_html1 = img_to_html('bia1.png', width="1306px", height="540px") 

css_code = """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .navbar a {
        text-decoration: none;
        color:  #FF8343;
        padding: 8px 16px;
        margin-top: 28px;
        font-size: 16px;
        font-weight: bold;
    }
    .navbar a:hover {
        color:  #FF8343;
        text-decoration: underline;
    }
    .logo {
        padding: 1px;
        margin-bottom: 50px;
    }
    .hero {
        background:  #FEEFDB;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: black;
        margin-bottom: 80px;
        padding: 180px;
    }
    .hero h1 {
        font-size: 48px;
        margin-bottom: 20px;
    }
    .hero p {
        font-size: 18px;
        color: #6F514A;
    }
    .download-btn {
        background-color: #FF8343;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 18px;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        margin-left: 25px;
    }
    .download-btn:hover {
        background-color: linear-gradient(174.6deg, rgb(252, 200, 191) 11.8%, rgb(254, 159, 160) 89.9%);
    }
    </style>
"""

# Chèn CSS vào Streamlit
st.markdown(css_code, unsafe_allow_html=True)

# st.markdown("""
#     <script>
#     document.addEventListener('DOMContentLoaded', function() {
#         document.querySelector('.download-btn').onclick = function() {
#             window.location.href = "/?page=trainghiem";
#         };
#     });
#     </script>
# """, unsafe_allow_html=True)

# Thanh điều hướng và hero section
st.markdown(f"""
    <div class="navbar">
        <div class="logo">
            {logo_html}
        </div>
        <div>
            <a href="http://localhost:8501/Home">Home</a>
            <a href="http://localhost:8501/Derminsight">Trải nghiệm Derm Insight</a>
            <a href="#services">About us</a>
            <a href="#projects">Vấn đề da liễu</a>
        </div>
    </div>

    <div class="hero" id="home">
        {bia_html1}
    </div>
""", unsafe_allow_html=True)
# <button class="download-btn" >THỬ NGAY</button>


col1, col2, col3= st.columns([0.5,0.1,0.4])

with col1:
        st.markdown('<p id="services", class="title", style= "margin-bottom: 20px;">DERM INSIGHT LÀ GÌ</p>', unsafe_allow_html=True)
        st.markdown('<p  style= "font-size: 18px; font-family:  "Times New Roman", Times, serif; ">DERM INSIGHT là một Website phân tích hình ảnh để giúp người dùng chuẩn đoán tình trạng da hiện tại mà không càn đến bệnh viện. Với công nghệ trí tuệ thông minh nhân tạo và bộ dữ liệu hơn 3000 ảnh. DERM INSIGHT có thể phát hiện bốn loại bệnh da liễu. (chàm, sừng, vẫy nến, mụn trứng cá nặng) trên làn da của bạn.</p>', unsafe_allow_html=True)
        st.markdown('<p style= "color: #FF8343;  font-weight: bold;font-size: 18px; margin-top: 15px; margin-bottom: 30px";>Hãy khám phá ngay!</p>', unsafe_allow_html=True)
        if st.button("THỬ NGAY"):
            st.switch_page("pages/Derminsight.py")
    

with col2:
        st.write("")

with col3:
        st.image("Screenshot 2024-10-28 at 18.27.04.png", width= 400)

    # button_thungay = st.button("THỬ NGAY", type="primary")
    #     # Kiểm tra nếu người dùng nhấn nút
    # if button_thungay:
    #     st.session_state.page = "trainghiem"

    # Hàm chuyển đổi ảnh thành base64
def img_to_base64(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    # Tạo mã HTML cho ảnh
muntrungca_base64 = img_to_base64('muntrungca.png')
muntrungca_html = f'<img src="data:image/png;base64,{muntrungca_base64}" style="width:100%; height:auto; border-radius: 5px;"/>'

benhcham_base64 = img_to_base64('benhcham.png')
benhcham_html = f'<img src="data:image/png;base64,{benhcham_base64}" style="width:100%; height:auto; border-radius: 5px;"/>'

benhvaynen_base64 = img_to_base64('banhvaynen.png')
benhvaynen_html = f'<img src="data:image/png;base64,{benhvaynen_base64}" style="width:100%; height:auto; border-radius: 5px;"/>'

benhdaysung_base64 = img_to_base64('daysung.png')
benhdaysung_html = f'<img src="data:image/png;base64,{benhdaysung_base64}" style="width:100%; height:auto; border-radius: 5px;"/>'


    # Định dạng CSS để tùy chỉnh giao diện
st.markdown("""
        <style>
            .title {
                font-size: 32px;
                font-weight: bold;
            }
            .subtitle {
                font-size: 18px;
                color: black;
                margin-top: -10px;
            }
            .container {
                display: flex;
                gap: 10px;
                justify-content: space-between;
                margin-top: 20px;
            }
            .card {
                position: relative;
                width: 25%;
                border-radius: 5px;
                overflow: hidden;
                text-align: left;
            }
            .card-content {
                position: absolute;
                bottom: 20px;
                left: 20px;
                color: white;
            }
            .card img {
                width: 100%;
                height: auto;
                display: block;
                border-radius: 5px;
            }
            .overlay {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                color: white;
                display: flex;
                align-items: flex-end;
                padding: 20px;
                box-sizing: border-box;
                border-radius: 5px;
            }
            .card-title {
                font-size: 30px;
                font-weight: bold;
                color: white;
                margin: 0;
            }
            .card-link {
                font-size: 16px;
                font-weight: bold;
                text-decoration: none; 
                margin-top: 5px;
            }
            .card-link:hover {
                color: black; 
                text-decoration: underline; /* Gạch chân khi hover */
            }
            .popup {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 80%;
                max-width: 500px;
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                z-index: 9999;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Hiển thị tiêu đề 
st.markdown('<p class="subtitle" style= "margin-top: 25px">THAM KHẢO THÊM</p>', unsafe_allow_html=True)
st.markdown('<p class="title", style= "margin-bottom: 15px";>TÌNH TRẠNG DA CỦA BẠN</p>', unsafe_allow_html=True)
    
st.write('Da là cơ quan lớn nhất của cơ thể, đóng vai trò như một hàng rào bảo vệ đầu tiên chống lại các tác nhân bên ngoài, từ vi khuẩn, virus cho đến các yếu tố môi trường như ánh nắng, bụi bẩn và hóa chất. Không chỉ là lớp vỏ bọc cơ thể, da còn tham gia vào quá trình điều chỉnh nhiệt độ, duy trì độ ẩm và cảm nhận các tác động vật lý từ môi trường.')
st.markdown('<p style= "color: #FF8343;  font-weight: bold;font-size: 18px; margin-top: 15px; margin-bottom: 30px";>Hãy khám phá bốn loại bệnh dưới đây để hiểu sâu hơn về làn da của bạn ! </p>', unsafe_allow_html=True)

    # Card 1: Mụn trứng cá
st.markdown(f"""
        <div id="projects" class="container">
            <div class="card">
                {muntrungca_html}
                <div class="overlay">
                    <div class="card-content">
                        <p class="card-title">MỤN TRỨNG CÁ</p>
                        <a href="http://localhost:8501/muntrungca" class="card-link" href="?show_popup=true">KHÁM PHÁ</a>
                    </div>
                </div>
            </div>
            <div class="card">
                {benhcham_html}
                <div class="card-content">
                    <p class="card-title">BỆNH CHÀM</p>
                    <a href="http://localhost:8501/benhcham" class="card-link">KHÁM PHÁ</a>
                </div>
            </div>
            <div class="card">
                {benhvaynen_html}
                <div class="card-content">
                    <p class="card-title">BỆNH VẨY NẾN</p>
                    <a href="http://localhost:8501/benhvaynen" class="card-link">KHÁM PHÁ</a>
                </div>
            </div>
            <div class="card">
                    {benhdaysung_html}
                <div class="card-content">
                    <p class="card-title">BỆNH DÀY SỪNG QUANG HOÁ</p>
                    <a href="http://localhost:8501/benhdaysung" class="card-link">KHÁM PHÁ</a>
                </div>
            </div>
        </div>

    """, unsafe_allow_html=True)

    # Kết thúc container
st.markdown('</div>', unsafe_allow_html=True)

    # Kiểm tra nếu người dùng đã nhấn vào "KHÁM PHÁ"
if st.session_state.get("show_popup"):
        # Nội dung của pop-up
        st.markdown("""
            <div class="popup">
                <h2>Thông tin về Mụn Trứng Cá</h2>
                <p>Đây là chi tiết thông tin về mụn trứng cá. Bạn có thể thêm nội dung chi tiết về sản phẩm, phương pháp điều trị, hoặc bất kỳ thông tin nào bạn muốn hiển thị ở đây.</p>
                <a href="?" style="display: inline-block; margin-top: 10px; padding: 10px 20px; background-color: #333; color: white; border-radius: 5px; text-decoration: none;">Đóng</a>
            </div>
        """, unsafe_allow_html=True)


# # CSS cho phần footer
# footer_css = """
#     <style>
#     .footer {
#         background-color: white;  
#         color: white;
#         padding: 1px ;
#         text-align: center;
#     }
#     .footer .container {
#         display: flex;
#         flex-direction: column;
#         justify-content: center;
#         align-items: center;
#     }
#     .footer-icons a {
#         margin-top: 1px;
#         margin-bottom: 10px;
#         color: #FF8343;
#         padding: 3px;  /* Giảm kích thước padding để icon nhỏ hơn */
#         border-radius: 50%;
#         font-size: 17px;  /* Giảm font-size để icon nhỏ hơn */
#         display: inline-block;
#         text-decoration: none;
#     }
#     .footer-icons a:hover {
#         color: #343a40;  /* Màu khi hover */
#     }
#     .footer-bottom {
#         background-color: #FFEADF;
#         padding: 10px;
#         width: 100%;
#         text-align: center;
#         font-size: 14px;
#         color: #503C37;;
#         font-weight: bold;
#     }
#     .footer-bottom a {
#         color: #503C37;
#         text-decoration: none;
#     }
#     </style>
# """

# # Thêm CSS vào ứng dụng
# st.markdown(footer_css, unsafe_allow_html=True)

# # HTML cho footer
# footer_html = """
# <div class="footer">
#     <div class="footer-bottom">
#         © 2024 Copyright:
#         <a>Derminsight.team@gmail.com</a>
#     </div>
#     <div class="container">
#         <div class="footer-icons">
#             <a href="#!" role="button"><i class="fab fa-facebook-f"></i></a>
#             <a href="#!" role="button"><i class="fab fa-twitter"></i></a>
#             <a href="#!" role="button"><i class="fab fa-google"></i></a>
#             <a href="#!" role="button"><i class="fab fa-instagram"></i></a>
#             <a href="#!" role="button"><i class="fab fa-linkedin-in"></i></a>
#             <a href="#!" role="button"><i class="fab fa-github"></i></a>
#         </div>
#     </div>
# </div>
# """

# # Thêm HTML vào ứng dụng
# st.markdown(footer_html, unsafe_allow_html=True)

# # Thêm link tới Font Awesome để hiển thị icon
# st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>', unsafe_allow_html=True)


footer_css = """
    <style>
    .footer {
        background-color: #FF8343;  /* Màu nền cam */
        color: white;
        padding: 10px;
        text-align: center;
    }
    .footer .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .footer-icons a {
        margin: 5px;
        color: black;
        border: 1px solid white;
        padding: 8px;  /* Giảm kích thước padding để icon nhỏ hơn */
        border-radius: 50%;
        font-size: 16px;  /* Giảm font-size để icon nhỏ hơn */
        display: inline-block;
        text-decoration: none;
    }
    .footer-icons a:hover {
        color: #343a40;  /* Màu khi hover */
    }
"""

# Thêm CSS vào ứng dụng
st.markdown(footer_css, unsafe_allow_html=True)




# # Thêm phần Footer
# st.markdown("""
# <style>
# @import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400);
# body {
#   font-family: 'Source Sans Pro', sans-serif;
#   font-weight: 300;
#   background-color: lightblue;
#   color: white;
# }
# .footer #button { 
#   width: 35px;
#   height: 35px;
#   border: #FF8343 12px solid;
#   border-radius: 35px;
#   margin: 0 auto;
#   position: relative;
#   transition: all 1s ease;
# }
# .footer #button:hover {
#   border: #3A3A3A 12px solid;
# }
# .footer {
#   bottom: 0;
#   left: 0;
#   position: fixed;
#   width: 100%;
#   height: 100px;
#   overflow: hidden;
#   margin: 0 auto;
#   transition: all 1s ease;
#   z-index: 999;
# }
# .footer:hover {
#   height: 100px;
# }
# .footer #container {
#   margin-top: 5px;
#   width: 100%;
#   height: 100%;
#   position: relative;
#   top: 0;
#   left: 0;
#   background: #FF8343;
# }
# .footer #cont {
#   position: relative;
#   top: -60px;
#   right: 190px;
#   width: 150px;
#   height: auto;
#   margin: 0 auto;
# }
# .footer_center {
#   width: 500px;
#   float: left;
#   text-align: center;
# }
# .footer h3 {
#   font-family: 'Helvetica';
#   font-size: 30px;
#   font-weight: bold;
#   margin-top: 70px;
#     color: white;
#   margin-left: 40px;
# }
# </style>

# <div class="footer">
#   <div id="button"></div>
#   <div id="container">
#     <div id="cont">
#       <div class="footer_center">
#         <h3>WELCOME TO DERM INSIGHT</h3>
#       </div>
#     </div>
#   </div>
# </div>
# """, unsafe_allow_html=True)

def img_to_html(img_path, width="00px", height="80px"):
    img_html = f"<img src='data:image/png;base64,{img_to_bytes(img_path)}' style='width:{width}; height:{height};'>"
    return img_html

# Sử dụng hàm img_to_html để mã hóa logo và hình ảnh bên phải
logo_html = img_to_html('logo.png', width="200px", height="200px")  # Thay đường dẫn này bằng logo của bạn


# Phần CSS
css_code = """
    <style>
    .footer {
        background-color: #f8f9fa;
        padding: 25px ;
        border-top: 1px solid #e9ecef;
        font-family: 'Arial', sans-serif;
    
    }
    .footer h4 {
        margin-left: 40x;
        font-size: 18px;
        color: #6c757d;

    }
    .footer .fix {
        margin-left: 60px;
        font-size: 18px;
        color: #6c757d;

    }

    .footer p, .footer address, .footer a {
        color: #6c757d;
        text-decoration: none;
        font-size: 16px;
        margin-right: 20px;
    }
    .footer a:hover {
        color:  #FF8343;
        text-decoration: underline;
    }
    .footer .widget-section {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        justify-content: space-between;
    }
    .footer .widget-section div {
        flex: 1;
        max-width: 600px;
    }
  
    .footer form input[type="email"] {
        width: 100%;
        padding: 0.5rem;
        margin-top: 10px;
        margin-bottom: 15px;
        border: 1px solid #ced4da;
        border-radius: 4px;
    }
    .footer form button {
        width: 100%;
        padding: 0.5rem;
        background-color: #FF8343;
        color: #fff;
        border: none;
        border-radius: 4px;
    }
     .footer-bottom {
        background-color: rgba(0, 0, 0, 0.2);
        padding: 15px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: white;
        font-weight: bold;
        margin: 5px;
    
    }
    .footer-bottom a {
        color: #6c757d;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
"""

# Chèn CSS vào Streamlit
st.markdown(css_code, unsafe_allow_html=True)

# Phần HTML
st.markdown(f"""
<footer class="footer">
  <section class="widget-section">
    <div >
      {logo_html}
    </div>
    <div>
      <h4>Get in Touch</h4>
      <address> 232/6 Vo Thi Sau Street, Ward 7, District 3, Ho Chi Minh City, Vietnam</address>
      <p><a href="tel:+84914031978">0914 031 978</a></p>
      <p><a href="mailto:derminsight.team@gmail.com">derminsight.team@gmail.com</a></p>
    </div>
    <div>
      <h4 class="fix">Learn More</h4>
      <ul style="list-style-type: none; padding-left: 0;">
        <li><a href="#!">About</a></li>
        <li><a href="#!">Contact</a></li>
        <li><a href="#!">Advertise</a></li>
        <li><a href="#!">Terms of Service</a></li>
        <li><a href="#!">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h4>Our Newsletter</h4>
      <p>Subscribe to our newsletter to get our news & discounts delivered to you.</p>
      <form action="#!">
        <input type="email" placeholder="Email Address" required>
        <button type="submit">Subscribe</button>
      </form>
    </div>
  </section>
  <div class="container">
        <div class="footer-icons">
            <a href="#!" role="button"><i class="fab fa-facebook-f"></i></a>
            <a href="#!" role="button"><i class="fab fa-twitter"></i></a>
            <a href="#!" role="button"><i class="fab fa-google"></i></a>
            <a href="#!" role="button"><i class="fab fa-instagram"></i></a>
            <a href="#!" role="button"><i class="fab fa-linkedin-in"></i></a>
            <a href="#!" role="button"><i class="fab fa-github"></i></a>
        </div>
    </div>
    <div class="footer-bottom">
        © 2024 Copyright:
        <a>derminsight.team@gmail.com</a>
    </div>
</footer>
"""
,unsafe_allow_html=True)

