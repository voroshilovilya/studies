var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Map("/home", appBuilder =>
{
    var time = DateTime.Now.ToShortTimeString();

    // ��������� ������ - ������� �� ������� ����������
    appBuilder.Use(async (context, next) =>
    {
        var timenow = DateTime.Now.ToShortTimeString();
        Console.WriteLine($"Time: {timenow}");
        await next();   // �������� ��������� middleware
    });
    
    appBuilder.Map("/index", Index); // middleware ��� "/home/index"
    appBuilder.Map("/about", About); // middleware ��� "/home/about"
    // middleware ��� "/home"
    appBuilder.Run(async context => await context.Response.WriteAsync($"Home Page\nTime: {time}"));
});

app.Run(async (context) => await context.Response.WriteAsync("Page Not Found"));

app.Run();

void Index(IApplicationBuilder appBuilder)
{
    appBuilder.Run(async context => await context.Response.WriteAsync("Index Page"));
}
void About(IApplicationBuilder appBuilder)
{
    appBuilder.Run(async context => await context.Response.WriteAsync("About Page"));
}