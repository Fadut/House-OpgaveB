using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTests
{
    [TestClass]
    public class HouseTests
    {
        // Using Chrome Driver.
        private static readonly string DriverLocation = "C:\\Users\\Faton\\source\\SeleniumDrivers\\"; // My drivers location on C drive.

        private static IWebDriver _driver;

        [ClassInitialize]
        public static void Setup(TestContext context)
        {
            _driver = new ChromeDriver(DriverLocation);
        }

        [ClassCleanup] 
        public static void Cleanup()
        {
            _driver.Dispose();
        }

        [TestMethod]
        public void TestHouse()
        {
            // Location of HTML file
            string url = "file:///C:\\Users\\Faton\\source\\repos\\OpgaveB\\Website\\index.html";
            _driver.Navigate().GoToUrl(url);

            Assert.AreEqual("Houses with REST API", _driver.Title);

            Thread.Sleep(1000);

            // Test Add House
            IWebElement addressInput = _driver.FindElement(By.Id("address"));
            addressInput.SendKeys("Test address, Gade xx");

            IWebElement yearInput = _driver.FindElement(By.Id("constructionYear"));
            yearInput.SendKeys("1979");

            IWebElement addButton = _driver.FindElement(By.Id("fetch-house"));
            addButton.Click();

            Thread.Sleep(1000);


        }
    }
}