
import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Tính lãi đơn và lãi kép",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề
st.title("💰 CÔNG CỤ TÍNH LÃI ĐƠN VÀ LÃI KÉP")
st.write("Chương trình tính giá trị tương lai dựa trên vốn ban đầu, lãi suất và số kỳ.")

st.divider()

# Nhập dữ liệu
st.subheader("1. Nhập thông tin")

c = st.number_input(
    "Vốn ban đầu (C):",
    min_value=0.0,
    value=100.0,
    step=10.0
)

i = st.number_input(
    "Lãi suất mỗi kỳ (%):",
    min_value=0.0,
    value=1.0,
    step=0.5
)

n = st.number_input(
    "Số kỳ (n):",
    min_value=1,
    value=3,
    step=1
)

# Chuyển lãi suất phần trăm thành số thập phân
interest_rate = i / 100

# Nút tính toán
if st.button("TÍNH KẾT QUẢ", type="primary"):

    # Tính lãi đơn
    simple_interest = c * (1 + interest_rate * n)

    # Tính lãi kép
    compound_interest = c * (1 + interest_rate) ** n

    st.divider()
    st.subheader("2. Kết quả tính toán")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Giá trị tương lai (Lãi đơn)",
            value=f"{simple_interest:,.2f}"
        )

    with col2:
        st.metric(
            label="Giá trị tương lai (Lãi kép)",
            value=f"{compound_interest:,.2f}"
        )

    st.divider()

    # So sánh kết quả
    difference = compound_interest - simple_interest

    st.subheader("3. So sánh")

    st.write(f"**Chênh lệch:** {difference:,.4f}")

    if compound_interest > simple_interest:
        st.success("Lãi kép có giá trị lớn hơn lãi đơn.")
    elif compound_interest == simple_interest:
        st.info("Lãi đơn và lãi kép có giá trị bằng nhau.")
    else:
        st.info("Lãi kép có giá trị nhỏ hơn lãi đơn.")

    # Hiển thị công thức
    st.subheader("4. Công thức")

    st.latex(r"FV_{\text{đơn}} = C(1+in)")

    st.latex(r"FV_{\text{kép}} = C(1+i)^n")
