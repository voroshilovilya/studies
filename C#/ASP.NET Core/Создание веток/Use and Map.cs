var builder = WebApplication.CreateBuilder();
var app = builder.Build();

app.Map("/home", appBuilder =>
{
    var time = DateTime.Now.ToShortTimeString();

    // логгируем данные - выводим на консоль приложения
    appBuilder.Use(async (context, next) =>
    {
        var timenow = DateTime.Now.ToShortTimeString();
        Console.WriteLine($"Time: {timenow}");
        await next();   // вызываем следующий middleware
    });
    
    appBuilder.Map("/index", Index); // middleware для "/home/index"
    appBuilder.Map("/about", About); // middleware для "/home/about"
    // middleware для "/home"
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