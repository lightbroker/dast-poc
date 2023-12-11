using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using DastPocTarget.Models;

namespace DastPocTarget.Controllers;

public class HomeController : Controller
{
    private readonly IConfiguration _config;

    public HomeController(IConfiguration config)
    {
        this._config = config;
    }

    [HttpGet]
    public IActionResult Index()
    {
        AppUser appUser = new AppUser
        {
            Message = "unauthenticated"
        };

        return View(appUser);
    }

    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Index([Bind("Username,Password,Message")] AppUser appUser)
    {
        bool validUsername = string.Equals(appUser.Username, this._config["AppUser:Username"]);
        bool validPassword = string.Equals(appUser.Password, this._config["AppUser:Password"]);

        appUser = new AppUser
        {
            Message = "authentication failed"
        };

        if (validUsername && validPassword)
        {
            appUser.Message = "logged in!";
        }

        return View(appUser);
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
