#ifndef GLWIDGET_H
#define GLWIDGET_H

#include <QtOpenGL>
#include <QWidget>

class GLWidget : public QWidget
{
    Q_OBJECT
public:
    explicit GLWidget(QWidget *parent = nullptr);

public slots:
    void toggleBackgroundColor(bool toBlack);

protected:
    void initializeGL();
    void resizeGL(int width, int height);
    void paintGL();

signals:

};

#endif // GLWIDGET_H
