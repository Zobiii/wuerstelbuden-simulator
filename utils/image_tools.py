from PyQt6.QtGui import QPixmap, QPainter, QPainterPath, QColor, QPen
from PyQt6.QtCore import Qt, QRectF, QSize


def create_rounded_framed_pixmap(
    image_path: str,
    size: QSize,
    radius: int = 16,
    border_color: QColor = QColor("white"),
    border_width: int = 3,
) -> QPixmap:

    original = QPixmap(image_path).scaled(
        size,
        Qt.AspectRatioMode.KeepAspectRatioByExpanding,
        Qt.TransformationMode.SmoothTransformation,
    )

    rounded = QPixmap(size)
    rounded.fill(Qt.GlobalColor.transparent)
    painter = QPainter(rounded)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)

    rect = QRectF(
        border_width,
        border_width,
        size.width() - 2 * border_width,
        size.height() - 2 * border_width,
    )

    path = QPainterPath()
    path.addRoundedRect(rect, radius, radius)
    painter.setClipPath(path)

    painter.drawPixmap(rect.toRect(), original)

    pen = QPen(border_color)
    pen.setWidth(border_width)
    painter.setPen(pen)
    painter.drawRoundedRect(rect, radius, radius)

    painter.end()
    return rounded
