# Kịch bản


***I. Thông tin các thành phần***

**1.Người dùng (User)**
- Người dùng có thể đăng kí tài khoản bằng email (không được trùng), thiết lập password.
- Quy định về pw : có ít nhất 8 kí tự, chứa cả chữ in hoa, chữ thường và số.
- Về thông tin cá nhân: 
    + Điền đầy đủ các trường : fullName, birthday
    + userName là unique
    + Có thể chọn chế dộ cho từng thông tin: công khai hoăc riêng tư
- Người dùng có thể quản lý và đăng các bài viết lên trang cá nhân và chọ chế độ công khai hoặc riêng tư.


**2.Nhóm (Group)**
- groupName là unique
- Mỗi User đều có thể tạo nhóm và quản lý nhóm dưới rol là admin:
    + Set trạng thái cho nhóm: public / private
    + Mời người khác tham gia nhóm
    + Duyệt yêu cầu tham gia
    + Gán vai trò (role)
    + Duyệt yêu cầu đăng bài


**3.Thành viên group (Member)**
- Mỗi thành viên trong nhóm có thể có nhiều role khác nhau : admin, member, moderator,...
- Các thành viên trong nhóm có thể đăng bài post, sửa, xoá bài viết của mình.
- Các thành viên có thể xem bài viết của người khác, comment và react.

**4.Post: bài đăng**
- Trước khi một bài viết được đăng trong nhóm , nó sẽ được gán là 'pending' và chờ người quyền hạn trong nhóm duyệt bài.
- Yêu cầu chờ duyệt bài của thành viên cũng có thể bị reject 

**5.Các role**
- Thông tin role được lưu trong bảng roles.

**6.Trạng thái tham gia nhóm**
- Thông tin trạng thái tham gia nhóm cuat thành viên được lưu trong join_status.


***II. Cách thức hoạt động***
**1.Đăng ký & Đăng nhập**
- Đăng kí tài khoản:
    + Người dùng tạo tài khoản bằng email và mật khẩu. Thiết lập các thông tin yêu cầu
    + Thông tin tài khoản được lưu trong bảng users
- Đăng nhập:
    + Sử dụng userName và mật khẩu để đăng nhập, hệ thống sẽ xác thực thông tin để cho phép truy cập.

**2.Quản lý nhóm**
- Tạo nhóm:
    + Người dùng có thể tạo nhóm mới và sẽ trở thành Admin của nhóm đó.
    + Thông tin về nhóm được lưu trong bảng groups
- Mời người dùng khác tham gia nhóm:
    + Người dùng đã tham gia nhóm hoặc Admin đều có quyền mời người dùng khác tham gia nhóm ( người dùng mời thì vẫn phải chờ duyệt từ Admin)
    + Người dùng được mời có thể chấp nhận lời mời hoặc từ chối lời mời
- Yêu cầu tham gia nhóm:
    + Người dùng có thể gửi yêu cầu tham gia nhóm
    + Yêu cầu này được lưu vào bảng requests 
- Phê duyệt tham gia nhóm và gán vai trò:
    + Admin và thành viên có quyền hạn có thể phê duyệt yêu cầu tham gia nhóm và gán vai trò cho thành viên khác.
- Quản lý thành viên trong nhóm:
    + Admin có quyền xoá nhóm
    + Thành viên nhóm có quyền tự động rời khỏi nhóm
    + Các thành viên có quyền hạn có thể xem danh sách thành viên trong nhóm cũng như có quyền xoá thành viên khỏi nhóm
    + 

**3.Quản lý bài viết** 
- Đăng bài trên trang cá nhân:
    + Người dùng có thể đăng bài trên trang cá nhân và chọn chế độ công khai, riêng tư hoặc hạn chế.
    + Thông tin bài đăng được lưu trong bảng posts
- Đăng bài trên nhóm
    + Thành viên trong nhóm có thể đăng bài viết mới 
    + Bài viết cần được chờ duyệt từ người có quyền hạn để được đăng lên nhóm
    + Thành viên có quyền xoá bài, sửa bài(cần duyệt lại)
- Duyệt bài:
    + Người có quyền hạn được tông báo về các bài viết đang chờ duyệt
    + Họ có quyền để duyệt đăng, từ chối hoặc yêu cầu chỉnh sửa bài viết.
- Xuất bản bài viết :
    + Khi bài viết đã được duyệt sẽ được hiển thị cho tất cả các thành viên trong nhóm
    + Các thành viên nhóm đều có quyền comment và react bài viết 




***III. Một số lưu ý cho cá nhân***

**1.Trên trang cá nhân**
- Khi đki tài khoản user cần nhập những thông tin yêu cầu.
- Khi đăng bài (post) trên trang cá nhân không cần qua queue_post, groupId = NULL
- User đc gửi yêu cầu tham gia nhóm
- Có thể xem nhóm mà user là admin 
    select admin* where user.id = '?'
- Có thể xem user là thành viên nhóm nào
    select member* where user.id = '?'
- Có thể xem các bài post của user trên trang cá nhân hoặc trong nhóm. 

**2.Trong group**
- Xem thông tin admin nhóm, số thành viên trong nhóm

- Các user muốn tham gia nhóm phải đợi để đc chấp nhận request từ admin

- Các member trong nhóm muốn đăng bài thì đợi được duyệt bài từ admin

- Các bài post có thể chứa hình ảnh , text. Các thành viên trong nhóm có thể comment, react bài post