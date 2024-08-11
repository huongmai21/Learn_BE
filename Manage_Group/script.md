# Kịch bản

***I. Thông tin bảng db***

**1.User**
- Mỗi user chứa thông tin id, username, email, pw, birthday(có thể NULL), status(trạng thái hiển thị thông tin cá nhân) và createdTime(dấu thời gian tạo xong tài khoản).
- Với id là khoá chính, id và email là unique(duy nhất).

**2.Group**
- Mỗi group chứa thông tin id,groupname,status(trạng thái hiển thị group) và createdTime(dấu thời gian tạo group).
- Với id là khoá chính và unique(duy nhất).

**3.Member: thành viên group**
- Mỗi member của một group chưa thông tin id, groupId, userId, role(user/admin/contributor...:có thể có nhiều role cùng 1 lúc), join_status(hình thức tham gia group) và joinTime(dấu thời gian tham gia nhóm).
- Với id là khoá chính. userId và groupId là khoá ngoại references từ  id của bảng users và groups_.

**4.Post: bài đăng**
- Với mỗi bài post chứa thông tin id, groupId(có thể NULL nếu bài đăng thuộc trang cá nhân), authorId, title(tiêu đề), content(nội dung bài), status(trạng thái hiển thị bài đăng, only chỉ có trên bài đăng trang cá nhân)


***II. Cách hoạt động***

**1.Trên trang cá nhân /user**
- Khi đki tài khoản user cần nhập những thông tin yêu cầu.
- Khi đăng bài (post) trên trang cá nhân không cần qua queue_post, groupId = NULL
- User đc gửi yêu cầu tham gia nhóm
- Có thể xem nhóm mà user là admin 
    Select admin* where user.id = '?'
- Có thể xem user là thành viên nhóm nào
    select member* where user.id = '?'
- Có thể xem các bài post của user trên trang cá nhân hoặc trong nhóm. 

**2.Trong group**
- Xem thông tin admin nhóm, số thành viên trong nhóm

- Các user muốn tham gia nhóm phải đợi để đc chấp nhận request từ admin

- Các member trong nhóm muốn đăng bài thì đợi được duyệt bài từ admin

- Các bài post có thể chứa hình ảnh , text. Các thành viên trong nhóm có thể comment , react bài post