-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 04, 2023 lúc 06:25 PM
-- Phiên bản máy phục vụ: 10.4.22-MariaDB
-- Phiên bản PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `httt`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `caseloi`
--

CREATE TABLE `caseloi` (
  `id` int(11) NOT NULL,
  `nhietdomaylanh` varchar(10000) DEFAULT NULL,
  `quatgioocucnong` varchar(255) DEFAULT NULL,
  `donghododien` varchar(255) DEFAULT NULL,
  `cotiengphatratumaynen` varchar(255) DEFAULT NULL,
  `comuimaylanh` varchar(255) DEFAULT NULL,
  `trangthaimaynen` varchar(255) DEFAULT NULL,
  `bieuhienluoiloc` varchar(255) DEFAULT NULL,
  `coxuathientuyet` varchar(255) DEFAULT NULL,
  `hoatdongdongdien` varchar(255) DEFAULT NULL,
  `trangthaimaylanhkhibat` varchar(255) DEFAULT NULL,
  `maychayvangunglientuc` varchar(255) DEFAULT NULL,
  `manhinhdieukhien` varchar(255) DEFAULT NULL,
  `nuoctrongongdan` varchar(255) DEFAULT NULL,
  `denbaoloi` varchar(255) DEFAULT NULL,
  `trangthaidieuhoakhiconguondien` varchar(255) DEFAULT NULL,
  `IDloi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `caseloi`
--

INSERT INTO `caseloi` (`id`, `nhietdomaylanh`, `quatgioocucnong`, `donghododien`, `cotiengphatratumaynen`, `comuimaylanh`, `trangthaimaynen`, `bieuhienluoiloc`, `coxuathientuyet`, `hoatdongdongdien`, `trangthaimaylanhkhibat`, `maychayvangunglientuc`, `manhinhdieukhien`, `nuoctrongongdan`, `denbaoloi`, `trangthaidieuhoakhiconguondien`, `IDloi`) VALUES
(1, 'không mát', 'chạy', 'chạy', 'nhẹ', 'mùi lạ', 'không chạy', 'bẩn', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 1),
(2, 'không mát', 'chạy', 'chạy', 'ồn', 'mùi lạ', 'không chạy', 'bẩn', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 1),
(3, 'không mát', 'chạy', 'chạy', 'nhẹ', 'mùi lạ', 'không chạy', 'bẩn', 'nhiều', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 1),
(4, 'không mát', 'không chạy', 'không chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 2),
(5, 'không mát', 'không chạy', 'không chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'tự động ngắt', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 2),
(6, 'không mát', 'không chạy', 'không chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 2),
(7, 'không mát', 'chạy', 'chạy', 'ồn', 'không mùi', 'không chạy', 'bình thường', 'ít', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 3),
(8, 'không mát', 'chạy', 'chạy', 'ồn', 'mùi lạ', 'không chạy', 'bình thường', 'ít', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 3),
(9, 'không mát', 'chạy', 'chạy', 'ồn', 'không mùi', 'không chạy', 'bẩn', 'ít', 'thấp hơn', 'tự động ngắt', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 3),
(10, 'không mát', 'chạy', 'chạy', 'ồn', 'không mùi', 'không chạy', 'bình thường', 'nhiều', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'có nhấp nháy', 'bình thường', 4),
(11, 'không mát', 'chạy', 'chạy', 'ồn', 'không mùi', 'không chạy', 'bình thường', 'nhiều', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 4),
(12, 'không mát', 'chạy', 'không chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 4),
(13, 'không mát', 'không chạy', 'chạy', 'ồn', 'không mùi', 'chạy', 'bình thường', 'ít', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'có', 'không có', 'bình thường', 5),
(14, 'không mát', 'không chạy', 'chạy', 'ồn', 'không mùi', 'chạy', 'bình thường', 'ít', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'có nhấp nháy', 'bình thường', 5),
(15, 'không mát', 'không chạy', 'không chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 5),
(16, 'mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'có', 'bình thường', 'bình thường', 'ngưng liên tục', 'lên hình', 'có', 'không có', 'bình thường', 6),
(17, 'chạy', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'không chạy', 'bình thường', 'có', 'bình thường', 'bình thường', 'ngưng liên tục', 'lên hình', 'có', 'không có', 'bình thường', 6),
(18, 'không mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'có', 'bình thường', 'bình thường', 'ngưng liên tục', 'lên hình', 'có', 'không có', 'bình thường', 6),
(19, 'mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'có', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'có nhấp nháy', 'bình thường', 7),
(20, 'không mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'có', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'có nhấp nháy', 'bình thường', 7),
(21, 'mát', 'chạy', 'chạy', 'nhẹ', 'mùi lạ', 'chạy', 'bình thường', 'có', 'thấp hơn', 'bình thường', 'bình thường', 'lên hình', 'không có', 'có nhấp nháy', 'bình thường', 7),
(22, 'mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'không lên hình', 'không có', 'không có', 'bình thường', 8),
(23, 'không mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'không lên hình', 'không có', 'không có', 'bình thường', 8),
(24, 'mát', 'không chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'không lên hình', 'không có', 'không có', 'bình thường', 8),
(25, 'không mát', 'chạy', 'chạy', 'ồn', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'không chạy', 9),
(26, 'không mát', 'không chạy', 'chạy', 'ồn', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'không chạy', 9),
(27, 'không mát', 'không chạy', 'không chạy', 'ồn', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'không chạy', 9),
(28, 'mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'tự động ngắt', 'ngưng liên tục', 'lên hình', 'không có', 'không có', 'bình thường', 10),
(29, 'không mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'bình thường', 'tự động ngắt', 'ngưng liên tục', 'lên hình', 'không có', 'không có', 'bình thường', 10),
(30, 'mát', 'chạy', 'chạy', 'nhẹ', 'không mùi', 'chạy', 'bình thường', 'ít', 'thấp hơn', 'tự động ngắt', 'ngưng liên tục', 'lên hình', 'không có', 'không có', 'bình thường', 10),
(35, 'mát', 'chạy', 'chạy', 'nhẹ', 'mùi lạ', 'không chạy', 'bẩn', 'ít', 'bình thường', 'bình thường', 'bình thường', 'lên hình', 'không có', 'không có', 'bình thường', 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `loivakhacphuc`
--

CREATE TABLE `loivakhacphuc` (
  `ID` int(11) NOT NULL,
  `loi` varchar(10000) NOT NULL,
  `giaiphap` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `loivakhacphuc`
--

INSERT INTO `loivakhacphuc` (`ID`, `loi`, `giaiphap`) VALUES
(1, 'dàn lạnh của máy lạnh hỏng', '- Vệ sinh hệ thống lọc gió và dàn lạnh định kỳ\r\n- Kiểm tra đường ống dẫn gas, bảng mạch, thông mạch của thiết bị bảo vệ, kiểm tra mối nối điện \r\n- xiết chặt lại…\r\n- Khi gặp trường hợp mùi hôi lạ: nên tắt máy và mở cửa phòng và quạt hút cho thông thoáng. Gas lạnh ở nồng độ cao sẽ gây choáng hoặc bất tỉnh nếu hít phải\r\n\r\n'),
(2, 'Dàn nóng của máy lạnh hỏng', 'Bảo trì dàn nóng và hệ thống tản nhiệt cũng như các dây kết nối.\r\nTiến hành vệ sinh máy lạnh định kỳ. \r\nTrong trường hợp cháy dây động cơ, hư hỏng quạt hoặc các linh kiện các thì bạn cần tiến hành thay mới.\r\nSạc đầy gas nếu thiếu hoặc rút bớt gas nếu thừa.\r\nSử dụng ổn áp để đảm bảo điện thế dòng điện được ổn định.'),
(3, 'Máy nén điều hoàn hỏng', 'Cố định lại đường ống tránh cho chúng va chạm với nhau.\r\nKiểm tra nơi đặt dàn nóng đã bằng phẳng hay chưa, vỏ máy nén có bị móp mép gây va chạm với các chi tiết bên trong hay không. Đồng thời, kiểm tra lại những bu lông ở dưới đáy máy xem có bị lỏng hay không. Sau đó, tiến hành kê lại máy cho ổn định và xiết chặt lại những bu lông bị lỏng\r\n'),
(4, 'quạt dàn lạnh bị hỏng', 'Cấp dầu cho linh kiện quạt\r\nKiểm tra board mạch, có thể sửa chữa hoặc thay mới\r\nThay Mô-tơ của quạt\r\n\r\n'),
(5, 'Quạt dàn nóng bị hỏng', 'Dùng đồng hồ đo điện kiểm tra xem mạch có bị ngắn hay có vấn đề gì không. Kiểm tra mọi đường dây của quạt xem có đứt đoạn nào không, nếu đứt hãy nối lại.\r\nKiểm tra bộ điều khiển xem các dây có hoạt động tốt không, xem đoạn nào bị đứt hay bị cháy không, các mạch trong bộ điều khiển có kết nối ổn định không. Nếu phát hiện có lỗi thì khắc phục ngay\r\n'),
(6, 'Van tiết lưu bị hỏng', '-Bọc lại đường bảo ôn: bọc lại ống dẫn gas bằng dây vải để tránh ống đồng dẫn gas bị đọng nước\r\n- Vệ sinh ống dẫn gas\r\n- Nếu đường ống bị gập, nứt có thể tiến hành hàn lại. Trong trường hợp bị gãy, đứt thì cần thay mới toàn bộ đường ống.\r\n- Thay mới đường ống dẫn gas\r\n'),
(7, 'Ống dẫn gas bị hỏng', ' -Bọc lại đường bảo ôn: bọc lại ống dẫn gas bằng dây vải để tránh ống đồng dẫn gas bị đọng nước\r\n	- Vệ sinh ống dẫn gas\r\n	- Nếu đường ống bị gập, nứt có thể tiến hành hàn lại. Trong trường hợp bị gãy, đứt thì cần thay mới toàn bộ đường ống.\r\n	- Thay mới đường ống dẫn gas\r\n'),
(8, 'Bộ điều khiển bị hỏng', '-Kiểm tra nguồn điện cấp cho máy lạnh: đã kết nối máy lạnh với nguồn điện hay chưa?\r\n- Kiểm tra pin lắp đúng vị trí hay chưa, hoặc thay pin mới nếu hết pin\r\n- Thay một điều khiển tương đồng\r\n'),
(9, 'Tụ điện bị hỏng', 'Máy lạnh nên được hoạt động ổn định nhất là trong những ngày nắng oi bức, tránh để hoạt động quá công suất\nTránh để máy lạnh hoạt động ở nhiệt độ thấp quá lâu\nTránh lắp đặt máy lạnh ở nơi thời tiết khắc nghiệt và nên có dụng cụ bảo vệ.\nCấp nguồn điện ổn định và không nên bật tắt thiết bị liên tục\n'),
(10, 'Máy lạnh hết gas', 'Nạp gas cho máy\r\nKiểm tra lại tải và điện thế dòng điện. Nếu tải không đủ thì bạn nên tắt bớt những thiết bị điện không sử dụng, hoặc sử dụng ổn áp để đảm bảo dòng điện được ổn định\r\nLiên hệ trung tâm bảo dưỡng để kiểm tra hoặc thay thế dàn ống dẫn\r\n\r\n');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `caseloi`
--
ALTER TABLE `caseloi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDloi` (`IDloi`);

--
-- Chỉ mục cho bảng `loivakhacphuc`
--
ALTER TABLE `loivakhacphuc`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `caseloi`
--
ALTER TABLE `caseloi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT cho bảng `loivakhacphuc`
--
ALTER TABLE `loivakhacphuc`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `caseloi`
--
ALTER TABLE `caseloi`
  ADD CONSTRAINT `caseloi_ibfk_1` FOREIGN KEY (`IDloi`) REFERENCES `loivakhacphuc` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
